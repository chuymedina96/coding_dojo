from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def index(request):

    context={
        "authors": Author.objects.all() 
    }

    return render(request,"books/index.html", context)

