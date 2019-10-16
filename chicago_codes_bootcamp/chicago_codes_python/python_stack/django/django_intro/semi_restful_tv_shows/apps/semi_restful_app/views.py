from django.shortcuts import render, HttpResponse, redirect
from .models import *


# Create your views here.
def root(request):

    return redirect("/shows")

def index(request):
    return render(request, "shows/index.html")


def shows(request):

    context = {
        "shows": Show.objects.all()
    }

    return render(request, "shows/shows_table.html", context)


def createShow(request):
    
    show                            = request.POST['title']
    network                         = request.POST['network']
    desc                            = request.POST['description']
    release                         = request.POST['release']
    request.session['title']        = show
    request.session['network']      = network
    request.session['description']  = desc
    request.session['release']      = release

    createdShow = Show.objects.last() 
    
    context ={
        "shows" : Show.objects.create(title=show, network=network, desc=desc, release=release)
    }
    return redirect(f"/shows/{createdShow.id}")


def viewShow(request, show_id):

    context = {
        "show": Show.objects.get(id=show_id)
    }

    return render(request, "shows/view_show.html", context)


def destroyShow(request, show_id):

    Show.objects.get(id=show_id).delete()

    return redirect("/shows")


def editShow(request, show_id):

    context={
        'show' : Show.objects.get(id=show_id)
    }
    return render(request, "shows/edit_show.html", context)


def updateShow(request, show_id):

    show            = Show.objects.get(id=show_id)
    show.title      = request.POST['title']
    show.network    = request.POST['network']
    show.release    = request.POST['release']
    show.desc       = request.POST['description']
    show.save()

    return redirect(f"/shows/{show_id}")
