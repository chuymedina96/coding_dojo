from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World")
def goodbye(request):
    return HttpResponse("See you later!")
def signup(request):
    return HttpResponse("Sign Up Here!")
def login(request):
    return HttpResponse("Login Here")
def new(request):
    return HttpResponse("Post new post here")
