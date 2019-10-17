from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
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
    
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')

    else:
        show                            = request.POST['title']
        network                         = request.POST['network']
        desc                            = request.POST['description']
        release                         = request.POST['release']

        Show.objects.create(title=show, network=network, desc=desc, release=release)

        createdShow = Show.objects.last()
        messages.success(request, "Show Created Successfully :)")

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

    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/{show_id}/edit')

    else:
        show = Show.objects.get(id = show_id)
        show.title      = request.POST['title']
        show.network    = request.POST['network']
        show.release    = request.POST['release']
        show.desc       = request.POST['description']
        show.save()
        messages.success(request, "Show Successfully Updated! :)")

    return redirect("/shows")
