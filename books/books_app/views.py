from django.shortcuts import render
from .models import Books

def show_all(req):
    books= Books.objects.all()
    context = {"books": books}
    return render(req, 'books_app/all.html', context)

def one_book (req, id):
    book= Books.objects.get(pk=id)
    context={"book":book}
    return render (req, "books_app/one_book.html", context)

def author_books(req, id):
    books=  Books.objects.filter(author_id= id)
    context = {"books":books}
    return render (req, "books_app/author.html", context)