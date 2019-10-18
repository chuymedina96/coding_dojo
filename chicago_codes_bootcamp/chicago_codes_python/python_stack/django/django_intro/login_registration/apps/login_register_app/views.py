from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request, "login-register/index.html")

def register(request):

    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        request.session['firstName']    = request.POST['firstName']
        request.session['lastName']     = request.POST['lastName']
        request.session['email']        = request.POST['email']
        request.session['password']     = request.POST['password']
        request.session['confirm']      = request.POST['confirm']
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')

    else:
        firstName                       = request.POST['firstName']
        lastName                        = request.POST['lastName']
        email                           = request.POST['email']
        password                        = request.POST['password']
        confirm                         = request.POST['confirm']


        # checking for duplicate data in database
        if(User.objects.filter(email=email).exists()):
            messages.error(request, "That email is already taken, sorry.")
            return redirect("/")

        else: 

            User.objects.create(firstName=firstName, lastName=lastName, email=email, password=password)

            createdUser = User.objects.last()

            request.session['user_id']   = createdUser.id

            messages.success(request, "User Created Successfully :)")

            return redirect("/success")

def success(request):

    if("user_id" not in request.session):
        messages.error(request, "You must be logged in in order to access this page. Rules are rules")
        return redirect("/")

    # if("loggedInUser_id" not in request.session):
    #     messages.error(request, "You must be logged in in order to access this page. Rules are rules")
    #     return redirect("/")

    else:

        loggedInUser    = User.objects.get(id=request.session["user_id"])
        # newSessionUser  = User.objects.get(id=request.session["loggedInUser_id"])

        context={

            "loggedInUser"  : loggedInUser,
            "all_users"     : User.objects.all()
        }
        return render(request, "login-register/success.html", context)

def logout(request):
    request.session.flush()

    messages.success(request, "Logged out :)")
    return redirect("/")


def login(request):

    email                           = request.POST['email']
    password                        = request.POST['password']
    
    user = User.objects.get(email=email)

    if user.password == password:
        request.session['user_id']   = user.id
        return redirect("/success")
    else:
        return redirect("/success")

    # if (User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists()):
    #     request.session['email']        = email
    #     request.session['password']     = password

    #     messages.error(request, "That email is already taken, sorry.")
    #     return redirect("/success")