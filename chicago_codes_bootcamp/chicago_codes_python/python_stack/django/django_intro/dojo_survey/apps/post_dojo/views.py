from django.shortcuts import render
def index(request):
    return render(request,"index.html")

def create_user(request):
    firstName_from_form             = request.POST['firstName']
    lastName_from_form              = request.POST['lastName']
    username_from_form              = request.POST['username']
    city_from_form                  = request.POST['city']
    state_from_form                 = request.POST['state']
    zip_from_form                   = request.POST['zip']
    gender_from_form                = request.POST['gender']
    # experience_less_from_form       = request.POST['less-one']
    # experience_one_three_from_form  = request.POST['one-three']
    # experience_three_five_from_form = request.POST['three-five']
    # experience_more_five_from_form  = request.POST['more-five']
    context = {
        "firstName_on_template"                 : firstName_from_form,
        "lastName_on_template"                  : lastName_from_form,
        "fullName_on_template"                  : username_from_form,
        "city_from_template"                    : city_from_form,
        "state_from_template"                   : state_from_form,
        "zip_from_template"                     : zip_from_form,
        "gender_from_template"                  : gender_from_form,
        # "experience_less_one_from_template"     : experience_less_from_form,
        # "experience_one_three_from_template"    : experience_one_three_from_form,
        # "experience_three_five_from_template"   : experience_three_five_from_form,
        # "experience_more_five_from_template"    : experience_more_five_from_form
    }
    return render(request,"results.html",context)


