from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    context={
        "authors": Author.objects.all(),
        "books"  : Book.objects.all()
    }
    return render(request, "book/index.html", context)


def authors(request):
    context={
        "authors": Author.objects.all(),
        "books"  : Book.objects.all()
    }
    return render(request, "author/index.html", context)


def viewAuthors(request, author_id):

    author = Author.objects.get(id=author_id)
    book   = Book.objects.all()

    context ={
        'author'  : author,
        "books"    : book
    }

    return render(request, "author/view.html", context)
    

def newAuthor(request):
    firstName                   = request.POST['firstName']
    lastName                    = request.POST['lastName']
    notes                       = request.POST['notes']
    request.session['firstName']= firstName
    request.session['lastName'] = lastName
    request.session['notes']    = notes

    context = {
        "author" : Author.objects.create(firstName=firstName, lastName=lastName, notes=notes)
    }

    return redirect("/authors", context)


def newBook(request):
    book                        = request.POST['title']
    describe                    = request.POST['describe']
    request.session['title']    = book
    request.session['describe'] = describe

    context = {
        "book" : Book.objects.create(title=book, desc=describe)
    }

    return redirect("/", context)


def viewBook(request, book_id):

    book    = Book.objects.get(id=book_id)
    authors = Author.objects.all()

    context ={
        'book'  : book,
        'authors': authors
    }

    return render(request, "book/view.html", context)


def addAuthorToBook(request):

    book                    = Book.objects.get(id=request.POST['book'])
    author                  = Author.objects.get(id=request.POST['author'])
    book.author.add(author)
    book.save()

    return redirect(f"/books/{book.id}")

def addBookToAuthor(request):

    author                  = Author.objects.get(id=request.POST['author'])
    book                    = Book.objects.get(id=request.POST['book'])
    author.books.add(book)
    author.save()

    return redirect(f"/authors/{author.id}")

