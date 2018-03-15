# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import BookMark, Word_Analytics
from main.forms import LinkBookMark, Search_Form
from django.template import loader
from django.utils import timezone
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from collections import defaultdict
from django.views.generic.base import TemplateView
# from django.urls import reverse
# from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import render
import requests
import re
import operator
from urllib.error import URLError
from .tasks import save_url_word_analytics
# Create your views here.

DEFAULT_PAGE_SIZE = 6


class IndexView(TemplateView):
    template_name = 'index.html'
    number_links = 1
    size = DEFAULT_PAGE_SIZE
    form = LinkBookMark()

    def post(self, request,  *args, **kwargs):
        if self.request.user.is_authenticated:
            if 'url' in self.request.POST:
                form = parse_link(request)
                try:
                    save_url_word_analytics.delay(self.request.user.username)
                except URLError:
                    pass
            elif 'delete_pk_id' in request.POST:
                delete_post(self.request.POST['delete_pk_id'])
            return HttpResponseRedirect("/")
        else:
            print("Non authenticated")
            return HttpResponseRedirect("/login/")

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            number_links = context['number_links'] if 'number_links' in context else self.number_links
            current_user = BookMark.objects.filter(user=self.request.user)
            page_output = Paginator(current_user.order_by('-pub_date'), self.size).page(number_links)
            context['page_output'] = page_output
            context['response_links'] = page_output.object_list
            context['form'] = self.form
            return context

def get_url(request, number_links):
    return index(request, number_links)


def get_search_results(request):
    template = loader.get_template('search_results.html')
    list_results_to_display = []
    search_string = ''

    if request.method == 'POST':
        if request.user.is_authenticated is True:
            _form = Search_Form(request.POST)
            if _form.is_valid():
                form_data = _form.cleaned_data
                search_string = form_data.get("search_parameters")
                if len(search_string) > 0:
                    search_string = clean_search_string(search_string)
                    list_results_to_display = get_searched_bookmarks(
                        search_string, request.user
                    )
            else:
                print("Nothing to search")

    page_output = Paginator(
        list_results_to_display, DEFAULT_PAGE_SIZE
    ).page(1)

    if len(search_string) > 0 and len(list_results_to_display) > 0:
        string_to_display = 'Результаты по вашему запросу: \"' + search_string + '\"'
    elif len(search_string) > 0 and len(list_results_to_display) == 0:
        string_to_display = "Извините, мы ничего не нашли по вашему запросу: \"" + search_string + '\"'
    else:
        string_to_display = "Извините, мы ничего не нашли по вашему запросу"

    context = {
        'search_string': string_to_display,
        'search_results': page_output.object_list,
        'page_output': page_output,
    }
    return HttpResponse(template.render(context, request))





def get_searched_bookmarks(_search_string, _user):

    user_bookmarks = BookMark.objects.filter(user=_user)
    bookmark_search_results = defaultdict(lambda: 0)

    for bookmark in user_bookmarks:
        results = Word_Analytics.objects.filter(
            bookmark=bookmark
        ).filter(
            word__in=(_search_string.split())
        )

        if len(results) > 0:
            for res in results:
                print(res)
                if bookmark.id in bookmark_search_results.keys():
                    bookmark_search_results[bookmark.id] += res.frequency
                else:
                    bookmark_search_results[bookmark.id]

    results_to_display = []
    if len(bookmark_search_results) > 0:
        # sort the results of search
        bookmark_search_results_sorted = sorted(
            bookmark_search_results.items(), key=operator.itemgetter(1),
            reverse=True
        )
        # add sorted results to a list to display
        for result in bookmark_search_results_sorted:
            results_to_display.append(BookMark.objects.get(id=result[0]))

    return results_to_display


def clean_search_string(search_string):
    search_string_cleaned = re.sub(
        '[^A-Za-zа-яА-Я0-9 ]', '', search_string.lower()
    )
    print(search_string_cleaned)
    return search_string_cleaned


def parse_link(request):
    form = LinkBookMark(request.POST)
    if form.is_valid():
        url = form.cleaned_data['url']
        html_preview = get_html(url)
        preview = get_meta_tags(html_preview)
        preview['url'] = url
        current_user = User.objects.get(username=request.user.username)
        preview['user'] = current_user
        # for key in preview:
        #     print('\t{}={}'.format(key, preview[key]))
        BookMark(pub_date=timezone.now(), **preview).save()
    return form


def get_meta_tags(html):
    """return dictionary meta tags"""
    dict_meta = {x: '' for x in ['title', 'image', 'description', 'site_name']}
    soup = BeautifulSoup(html, 'html.parser')
    for key in dict_meta:
        soup_find = soup.find('meta', property='og:' + key)
        if soup_find:
            dict_meta[key] = soup_find['content']
            continue
        soup_find = soup.find('meta', attrs={'name': key})
        if soup_find:
            dict_meta[key] = soup_find['content']
    return dict_meta


def get_html(url):
    from requests.exceptions import ConnectionError, ConnectTimeout
    headers = ''
    if 'vk.com' in url:
        # vk.com url is very strange, because without headers is not works
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
        }
    try:
        r = requests.get(url=url, headers=headers, timeout=5)
    except (ConnectTimeout, ConnectionError):
        return ''
    if r.status_code == 200:
        return r.text


def delete_post(pk_id):
    BookMark.objects.get(pk=pk_id).delete()
    return True


from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts


class GenerateRandomUserView(FormView):
    template_name = 'book/generate_random_users.html'
    form_class = GenerateRandomUserForm
    initial = {'key': 'value'}

    def form_valid(self, form):
        total = form.cleaned_data.get('total')

        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')

        return redirect('generate')

    def get(self, request, *args, **kwargs):
        users = User.objects.all().order_by('-date_joined')
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'users': users})

    def post(self, request, *args, **kwargs):
        users = User.objects.all().order_by('-date_joined')
        print(users)
        form = self.form_class(request.POST)
        if form.is_valid():
            self.form_valid(form)

        return render(request, self.template_name, {'form': form, 'users': users})
