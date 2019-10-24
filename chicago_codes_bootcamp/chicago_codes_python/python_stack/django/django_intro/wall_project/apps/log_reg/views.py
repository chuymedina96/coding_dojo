from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    if 'logged' not in request.session:
        request.session['logged'] = False
    return render(request, 'log_reg/index.html')

def register(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('/')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password_reg'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(username = request.POST['username'], email = request.POST['email_reg'], password = pw_hash)
        request.session['user_id'] = new_user.id
        request.session['logged'] = True
        return redirect('/wall/')

def login(request):
    errors = User.objects.log_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='login')
        return redirect('/')
    else:
        try:
            user = User.objects.get(email=request.POST['email_log'])
            request.session['user_id'] = user.id
            request.session['logged'] = True
            return redirect('/wall/')
        except:
            messages.error(request, 'Email not found. Please register.', extra_tags='login')
            return redirect('/')

def success(request):
    if request.session['logged'] == True:
        logged_user = User.objects.get(id = request.session['user_id'])
        context = {
            'user': logged_user
        }
        return render(request, 'log_reg/success.html', context)
    else:
        messages.error(request, 'Please log in.', extra_tags='login')
        return redirect('/')

def logout(request):
    request.session['logged'] = False
    request.session['user_id'] = 0
    return redirect('/')