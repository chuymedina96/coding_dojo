from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def indexTwo(request):
    context = {
        "title": "My Travel List",
        "year": 2019,
        "cities": ["Chicago", "Denver", "Miami"],
        "activities": ["Eat", "Hike", "Swim"]
    }
    return render(request, "simple_html_templates/index.html", context)