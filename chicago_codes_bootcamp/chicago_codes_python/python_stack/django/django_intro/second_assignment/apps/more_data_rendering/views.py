from django.shortcuts import render

def index(request):
    context = { 
        "students" : [
            {'name' : 'Michael', 'age' : 35},
            {'name' : 'John', 'age' : 30 },
            {'name' : 'Mark', 'age' : 25},  
            {'name' : 'KB', 'age' : 27}
        ]
    }
    return render(request, "more_data_rendering/index.html", context)
