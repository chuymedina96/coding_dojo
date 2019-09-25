from django.shortcuts import render
    
def index(request):
    context = {
        "phrase" : "hello",
        "list" : [0,1,2,3,4,5]
    }
    return render(request, "template_data_practice/index.html", context)
