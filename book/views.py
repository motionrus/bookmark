from django.shortcuts import render
from django.http import HttpResponse
from book.models import Translate
from django.core.paginator import Paginator
# Create your views here.

PERIOD_PAGE = 50


def index(request):
    context = {'book': 'imlegend'}
    return render(request, 'book/book.html', context)


def imlegend(request, page=1):
    page = int(page)
    objects = Translate.objects.all()
    p = Paginator(list(objects), PERIOD_PAGE)
    render_page = p.page(page)
    if render_page.number -1 > 1:
        render_page.has_pre_previews = True
        render_page.pre_previous_page_number = render_page.number - 2
    if render_page.number + 1 < render_page.paginator.num_pages:
        render_page.has_post_next = True
        render_page.post_next_page_number = render_page.number + 2
#    p.has_post_next = Paginator.validate_number(Paginator, number=page+2)
    context = {'page': render_page, 'paginator': p}
    return render(request, 'book/legend.html', context)
