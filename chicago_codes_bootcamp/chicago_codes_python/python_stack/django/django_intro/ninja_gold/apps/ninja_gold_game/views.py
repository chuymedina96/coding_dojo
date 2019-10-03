from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):

    if 'counter' not in request.session:
        request.session["counter"] = 0

    unique_id    = get_random_string(length=23, allowed_chars='abcdefghijklmnopqrstuvwxyz')

    context ={
        'counter': request.session["counter"],
        'session': request.session,
        'number' : unique_id
    }

    return render(request, "index.html", context)


def process(request):
    print("In the process method...")

    building_from_form  = request.POST['building']
    request.session['building'] = building_from_form

    if request.POST['building'] == 'farm':
        request.session["counter"] += 15
        print("fewfewfu22**")

    elif request.POST['building'] == 'cave':
        request.session["counter"] += 10
        print("ffe")

    elif request.POST['building'] == 'house':
        request.session["counter"] += 3

    elif request.POST['building'] == 'casino':
        request.session["counter"] += 50



    return redirect("/")

def destroy_session(request):
    request.session.pop["counter"]
    return redirect("/")
