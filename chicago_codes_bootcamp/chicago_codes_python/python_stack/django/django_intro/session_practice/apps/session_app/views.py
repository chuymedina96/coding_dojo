from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session["counter"] = 0
    else:
        request.session["counter"] +=1

    context ={
        'counter': request.session["counter"],
        'session': request.session
    }

    return render(request, "session_templates/index.html", context)

def destroy_session(request):
    request.session.pop("counter")
    return redirect("/")

def add_two(request):
    request.session['counter'] +=1
    return redirect("/")



