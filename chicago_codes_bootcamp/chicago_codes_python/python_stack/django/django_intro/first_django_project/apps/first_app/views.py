from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse
def index(request):
    return render(request, 'index.html')
def sign(request):
    return render(request, 'signin.html')
def login(request):
    return HttpResponse("Login Here")
def goodbye(request):
    return HttpResponse("goodbye")



