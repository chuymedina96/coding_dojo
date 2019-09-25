from django.shortcuts import render
from time import gmtime, strftime, localtime

def index(request):
    context = {
        "time": strftime("%a, %d %b %Y %I:%M:%S", localtime())
    }
    return render(request,'time_display_templates/index.html', context)

