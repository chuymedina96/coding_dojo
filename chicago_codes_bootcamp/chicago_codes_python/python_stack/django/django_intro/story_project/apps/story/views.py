from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "story_templates/index.html")

def story(request):
    name_from_form              = request.POST['name']
    radio_from_form             = request.POST['character']
    request.session['name']     = name_from_form
    request.session['character'] =radio_from_form

    context={
        "name_from_template": name_from_form,
        "radio_from_template": radio_from_form,
        "request_name": request.session['name'],
        "request_character": request.session['character'],
    }
    return render(request, "story_templates/begin.html", context)

def cop1(request):
    return render(request, "story_templates/cop/index.html")

