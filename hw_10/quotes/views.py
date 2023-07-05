from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator

from .models import Author, Tag, Quote

from .utils import get_mongodb


def main(request, page=1):
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all()
    per_page = 5
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def about_author(request, author_id):
    author = Author.objects.get(pk=author_id)
    # return HttpResponse(f' About Author {author.fullname}')
    return render(request, 'quotes/about_author.html', {'author': author})
# def about_author(request):
#
#     return HttpResponse('About Author')

#
# def about_author(request, _id):
#
#     author = Author.objects.get(pk=_id)
#     return render(request, "quotes/author.html", {"author": author})