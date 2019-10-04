from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import random

# Create your views here.
def index(request):

    if 'counter' not in request.session:
        request.session["counter"] = 0

    context ={
        'counter': request.session["counter"],
        'session': request.session,
    }

    return render(request, "index.html", context)



def process(request):

    building_from_form  = request.POST['building']
    request.session['building'] = building_from_form

    if request.POST['building'] == 'farm':

        randFarm = random.randint(10,20)
        request.session["counter"] += randFarm

    elif request.POST['building'] == 'cave':

        randCave = random.randint(5,10)
        request.session["counter"] += randCave

    elif request.POST['building'] == 'house':

        randHouse = random.randint(2,5)
        request.session["counter"] += randHouse

    elif request.POST['building'] == 'casino':
        chance = random.randint(-50,50)

        request.session["counter"] += chance

    context ={
        "activity" : request.session['building'],
    }

    return redirect("/", context)



def destroy_session(request):
    request.session.clear()
    return redirect("/")
