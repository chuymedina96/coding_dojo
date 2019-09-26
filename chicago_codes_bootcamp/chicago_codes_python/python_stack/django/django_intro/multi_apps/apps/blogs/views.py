from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect("/blogs")
def getBlog(request, number):
    return HttpResponse(f"placeholder to display blog number: {number} with a method named 'show'")
def editBlog(request, number):
    return HttpResponse(f"placeholder to edit blog {number} with a method named 'edit'")
def destroy(request, number):
    return redirect("/blogs")


