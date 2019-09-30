from django.shortcuts import render
from time import localtime, strftime
from datetime import datetime

def index(request):
    context = {
        "time": strftime("%a, %d %b %Y %I:%M:%S", localtime()),
        "date": strftime("%b %d, %Y", localtime()),
        "now" : datetime.now(),
    }
    return render(request,'time_display_templates/index.html', context)