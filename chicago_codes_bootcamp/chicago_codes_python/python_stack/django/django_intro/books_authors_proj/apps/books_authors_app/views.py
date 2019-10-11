from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def index(request):
    context={
        "authors": Author.objects.all(),
        "books"  : Book.objects.all()
    }
    return render(request, "book/index.html")