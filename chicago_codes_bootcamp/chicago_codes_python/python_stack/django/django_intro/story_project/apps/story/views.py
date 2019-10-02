from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "story_templates/index.html")

def story(request):
    name_from_form                  = request.POST['name']
    radio_from_form                 = request.POST['character']
    request.session['name']         = name_from_form
    request.session['character']    = radio_from_form

    context={
        "name_from_template"        : name_from_form,
        "radio_from_template"       : radio_from_form,
        "request_name"              : request.session['name'],
        "request_character"         : request.session['character'],
    }
    if request.POST['character'] == 'cop':
        return render(request, "story_templates/cop/index.html", context)
    else:
        return redirect("/robber1")


def cop2(request):
    food_from_form              = request.POST['food']
    vehicle_from_form           = request.POST['vehicle']
    music_from_form             = request.POST['music']
    behavior_from_form          = request.POST['behavior']
    request.session['food']     = food_from_form
    request.session['vehicle']  = vehicle_from_form
    request.session['music']    = music_from_form
    request.session['behavior'] = behavior_from_form,
    

    context ={
        "food_from_template"        : request.session['food'],
        "vehicle_from_template"     : request.session['vehicle'],
        "music_from_template"       : request.session['music'],
        "behavior_from_form"        : request.session['behavior'],
        "request_name"              : request.session['name'],
        "request_character"         : request.session['character']

    }
    return render(request, "story_templates/cop/story1.html", context)

def cop3(request):

    context ={
        "food_from_template"        : request.session['food'],
        "vehicle_from_template"     : request.session['vehicle'],
        "music_from_template"       : request.session['music'],
        "behavior_from_form"        : request.session['behavior'],
        "request_name"              : request.session['name'],
        "request_character"         : request.session['character']
    }
    
    return render(request, "story_templates/cop/story2.html", context)

def cop4(request):

    context ={
        "food_from_template"        : request.session['food'],
        "vehicle_from_template"     : request.session['vehicle'],
        "music_from_template"       : request.session['music'],
        "behavior_from_form"        : request.session['behavior'],
        "request_name"              : request.session['name'],
        "request_character"         : request.session['character']
    }
    return render(request, "story_templates/cop/story3.html", context)


def robber1(request):
    context ={
        "request_name"              : request.session['name'],
        "request_character"         : request.session['character']
    }
    return render(request,"story_templates/robber/index.html", context)

def robber2(request):
    return render(request, "story_templates/robber/story1.html")

def robber3(request):
    return render(request, "story_templates/robber/story2.html")
    
def robber4(request):
    return render(request, "story_templates/robber/story3.html")

