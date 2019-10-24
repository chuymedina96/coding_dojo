from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
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
        hash_pw                         = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
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

            User.objects.create(firstName=firstName, lastName=lastName, email=email, password=hash_pw)

            createdUser = User.objects.last()

            request.session['user_id']   = createdUser.id

            messages.success(request, "User Created Successfully :)")

            return redirect("/wall")

def success(request):

    if("user_id" not in request.session):
        messages.error(request, "You must be logged in in order to access this page. Rules are rules")
        return redirect("/")

    # if("loggedInUser_id" not in request.session):
    #     messages.error(request, "You must be logged in in order to access this page. Rules are rules")
    #     return redirect("/")

    else:

        loggedInUser    = User.objects.get(id=request.session["user_id"])

        context={
            "loggedInUser"  : loggedInUser,
            "all_users"     : User.objects.all(),
            "all_messages"  : Message.objects.all().order_by("-created_at"),
            
        }
        return render(request, "login-register/wall.html", context)

def logout(request):
    request.session.flush()

    messages.success(request, "Logged out :)")
    return redirect("/")


def login(request):

    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        request.session['email']        = request.POST['email']
        request.session['password']     = request.POST['password']
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        email                           = request.POST['email']
        password                        = request.POST['password']
        
        user_set = User.objects.filter(email=email)
        user = user_set[0]

        if bcrypt.checkpw(password.encode(), user.password.encode()):
            request.session['user_id']   = user.id
            messages.success(request, f"Welcome back, {user.firstName}")
            return redirect("/wall")
        else:   
            messages.error(request, "Password did not match with any User in database, sorry try again!")
            return redirect("/wall")

    # if (User.objects.filter(email=email).exists() and User.objects.filter(password=password).exists()):
    #     request.session['email']        = email
    #     request.session['password']     = password

    #     messages.error(request, "That email is already taken, sorry.")
    #     return redirect("/success")

def newMessage(request):

    message = request.POST['message']

    userMessage = Message.objects.create(message=message)
    user = User.objects.get(id=request.session['user_id'])
    user.messages.add(userMessage)
    # something to target user and save them to a variable
    #something to add the message to them, then save
    user.save()
    messages.success(request, "Message created successfully")

    return redirect("/wall")

def createComment(request):

    comment  = request.POST['comment']
    
    userComment = Comment.objects.create(comment=comment, message=Message.objects.get(id=request.POST['message_id']), user=User.objects.get(id=request.session['user_id']))

    userComment.save()

    return redirect("/wall")







    


