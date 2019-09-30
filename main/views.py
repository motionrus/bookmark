import operator
import re
from collections import defaultdict
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.template import loader
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from main.forms import LinkBookMark, SearchForm
from main.models import BookMark, Word_Analytics
from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts

DEFAULT_PAGE_SIZE = 6
DEFAULT_IMAGE_URL = "static/img/bookmark.jpg"


class IndexView(TemplateView):
    template_name = "index.html"
    number_links = 1
    size = DEFAULT_PAGE_SIZE
    form = LinkBookMark()
    cleaned_data_url = ""

    def post(self, request):
        form = LinkBookMark(request.POST)

        if self.request.user.is_authenticated:
            if "url" in self.request.POST:
                if form.is_valid():
                    self.cleaned_data_url = form.cleaned_data["url"]
                    BookMark(pub_date=timezone.now(), **self.get_meta(request)).save()
                    # FIXME: нужно использовать celery
                    # try:
                    #     save_url_word_analytics.delay(self.request.user.username)
                    # except URLError:
                    #     pass
            elif "delete_pk_id" in request.POST:
                BookMark.objects.get(pk=self.request.POST["delete_pk_id"]).delete()
            return HttpResponseRedirect("/")
        else:
            print("Non authenticated")
            return HttpResponseRedirect("/login/")

    def get_context_data(self, **kwargs):
        from django.core.paginator import EmptyPage
        from django.http import Http404
        context = super(IndexView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            number_links = context["number_links"] if "number_links" in context else self.number_links
            current_user = BookMark.objects.filter(user=self.request.user)
            try:
                page_output = Paginator(current_user.order_by("-pub_date"), self.size).page(number_links)
            except EmptyPage:
                raise Http404

            context["page_output"] = page_output
            context["response_links"] = page_output.object_list
            context["form"] = self.form
            return context

    def get_meta(self, request):
        url = self.cleaned_data_url
        image_url = request.build_absolute_uri() + DEFAULT_IMAGE_URL
        dict_meta = {
            "title": urlparse(url).netloc,
            "image": image_url,
            "description": "",
            "site_name": "",
            "url": url,
            "user": User.objects.get(username=request.user.username)
        }
        html = IndexView.get_html(url)
        soup = BeautifulSoup(html, "html.parser")

        for key in dict_meta:
            soup_find = soup.find("meta", property="og:" + key) or soup.find("meta", attrs={"name": key})
            if soup_find:
                if key == "image" and not LinkBookMark({"url": soup_find["content"]}).is_valid():
                    soup_find["content"] = image_url
                dict_meta[key] = soup_find["content"]
        return dict_meta

    @staticmethod
    def get_html(url):
        from requests.exceptions import ConnectionError, ConnectTimeout
        headers = ""
        if "vk.com" in url:
            # vk.com url is very strange, because without headers is not works
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"
            }
        try:
            r = requests.get(url=url, headers=headers, timeout=5)
        except (ConnectTimeout, ConnectionError):
            return ""
        if r.status_code == 200:
            return r.text


def get_search_results(request):
    template = loader.get_template("search_results.html")
    list_results_to_display = []
    search_string = ""

    if request.method == "POST":
        if request.user.is_authenticated is True:
            _form = SearchForm(request.POST)
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
        string_to_display = "Результаты по вашему запросу: " + search_string
    elif len(search_string) > 0 and len(list_results_to_display) == 0:
        string_to_display = "Извините, мы ничего не нашли по вашему запросу: " + search_string
    else:
        string_to_display = "Извините, мы ничего не нашли по вашему запросу"

    context = {
        "search_string": string_to_display,
        "search_results": page_output.object_list,
        "page_output": page_output,
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
        "[^A-Za-zа-яА-Я0-9 ]", "", search_string.lower()
    )
    return search_string_cleaned


class GenerateRandomUserView(FormView):
    template_name = "book/generate_random_users.html"
    form_class = GenerateRandomUserForm
    initial = {"key": "value"}

    def form_valid(self, form):
        total = form.cleaned_data.get("total")

        create_random_user_accounts.delay(total)
        messages.success(self.request, "We are generating your random users! Wait a moment and refresh this page.")

        return redirect("generate")

    def get(self, request, *args, **kwargs):
        users = User.objects.all().order_by("-date_joined")
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form, "users": users})

    def post(self, request, *args, **kwargs):
        users = User.objects.all().order_by("-date_joined")
        form = self.form_class(request.POST)
        if form.is_valid():
            self.form_valid(form)

        return render(request, self.template_name, {"form": form, "users": users})
