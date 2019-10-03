from django.shortcuts import render, HttpResponse, redirect

# Views start here.

def index(request):

    return render(request, "story_templates/index.html")


def story(request):

    name_from_form                  = request.POST['name']
    radio_from_form                 = request.POST['character']
    gender_from_form                = request.POST['gender']
    request.session['name']         = name_from_form
    request.session['character']    = radio_from_form
    request.session['gender']       = gender_from_form

    context = {

        "name_from_template"        : name_from_form,
        "radio_from_template"       : radio_from_form,
        "request_name"              : request.session['name'],
        "request_character"         : request.session['character'],
        "gender"                    : request.session['gender']

    }

    if request.POST['character'] == 'cop':
        return render(request, "story_templates/cop/index.html", context)
    else:
        return render(request, "story_templates/robber/index.html", context)


def cop2(request):

    food_from_form                  = request.POST['food']
    vehicle_from_form               = request.POST['vehicle']
    music_from_form                 = request.POST['music']
    request.session['food']         = food_from_form
    request.session['vehicle']      = vehicle_from_form
    request.session['music']        = music_from_form
    

    context = {

        "food_from_template"        : request.session['food'],
        "vehicle_from_template"     : request.session['vehicle'],
        "music_from_template"       : request.session['music'],
        "request_name"              : request.session['name'],
        "request_character"         : request.session['character'],
        "gender"                    : request.session['gender']

    }

    return render(request, "story_templates/cop/story1.html", context)


def cop3(request):

    context ={
        "food_from_template"        : request.session['food'],
        "vehicle_from_template"     : request.session['vehicle'],
        "music_from_template"       : request.session['music'],
        "request_name"              : request.session['name'],
        "request_character"         : request.session['character'],
        "gender"                    : request.session['gender']
    }
    
    return render(request, "story_templates/cop/story2.html", context)


def cop4(request):

    context ={

        "food_from_template"        : request.session['food'],
        "vehicle_from_template"     : request.session['vehicle'],
        "music_from_template"       : request.session['music'],
        "request_name"              : request.session['name'],
        "request_character"         : request.session['character'],
        "gender"                    : request.session['gender']
    }

    return render(request, "story_templates/cop/story3.html", context)


def robber2(request):

    time_from_form                  = request.POST['time']
    rent_from_form                  = request.POST['rent']
    years_from_form                 = request.POST['years']
    transport_from_form             = request.POST['transport']
    request.session['time']         = time_from_form
    request.session['rent']         = rent_from_form
    request.session['years']        = years_from_form
    request.session['transport']    = transport_from_form

    context = {

        "request_name"              : request.session['name'],
        "request_character"         : request.session['character'],
        "time"                      : request.session['time'],
        "rent"                      : request.session['rent'],
        "years"                     : request.session['years'],
        "transport"                 : request.session['transport'],
        "gender"                    : request.session['gender']
        
    }
    return render(request, "story_templates/robber/story1.html", context)


def robber3(request):

    context = {

        "request_name"              : request.session['name'],
        "request_character"         : request.session['character'],
        "time"                      : request.session['time'],
        "rent"                      : request.session['rent'],
        "years"                     : request.session['years'],
        "transport"                 : request.session['transport'],
        "gender"                    : request.session['gender']
        
    }

    return render(request, "story_templates/robber/story2.html", context)
    

def robber4(request):

    context = {

        "request_name"              : request.session['name'],
        "request_character"         : request.session['character'],
        "time"                      : request.session['time'],
        "rent"                      : request.session['rent'],
        "years"                     : request.session['years'],
        "transport"                 : request.session['transport'],
        "gender"                    : request.session['gender']
        
    }

    return render(request, "story_templates/robber/story3.html", context)

