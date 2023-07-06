from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator

from .models import Author, Tag, Quote
from .forms import AddAuthorForm, AddQuoteForm

from .utils import get_mongodb


def main(request, page=1):
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all()
    per_page = 5
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    context = {'quotes': quotes_on_page, 'title': 'Quotes'}
    return render(request, 'quotes/index.html', context= context)


def about_author(request, author_id=1):
    author = Author.objects.get(pk=author_id)
    # return HttpResponse(f' About Author {author.fullname}')
    return render(request, 'quotes/about_author.html', {'author': author, 'title': 'About Author'})


def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:root")
            print(form.cleaned_data)
            print(form.cleaned_data["fullname"])
        else:
            return render(request, 'quotes/author.html', {'form': form, 'title': 'New Author'})
    return render(request, 'quotes/author.html', {'form': AddAuthorForm(), 'title': 'New Author'})

    # author = Author.objects.get(pk=author_id)
    # return HttpResponse(' Add!!  About Author ')
    # return render(request, 'quotes/add_author.html', {'author': author, 'title': 'About Author'})


def add_quote(request):
    if request.method == 'POST':
        print("quote!!!")
        form = AddQuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:root")
            print(form.cleaned_data)
            print(form.cleaned_data["name"])
        else:
            return render(request, 'quotes/quote.html', {'form': form, 'title': 'New Quote'})
    return render(request, 'quotes/quote.html', {'form': AddQuoteForm(), 'title': 'New Quote'})


def show_quote(request, tag_id, page=1):
    quotes = Quote.objects.filter(tags=tag_id).all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    context = {'quotes': quotes_on_page, 'title': 'Quotes fo tag'}
    return render(request, 'quotes/index.html', context=context)
