from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    
    if 'counter' not in request.session:
        request.session["counter"] = 0
    else:
        request.session["counter"] +=1

    unique_id = get_random_string(length=14)

    context ={
        'counter'       : request.session["counter"],
        'session'       : request.session,
        "random_word"   : unique_id
    }
    return render(request, "index.html", context)


def reset(request):
    request.session.pop("counter")
    return redirect("/random_word")

def generate(request):
    request.session['counter'] +=1
