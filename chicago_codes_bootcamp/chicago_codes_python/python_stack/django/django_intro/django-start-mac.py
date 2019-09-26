import time
import sys, os

projectTitle = input("What would you like to name your new Django project: ")
print(f"Cool, your project is called {projectTitle}")
print("Generating new Django project")
django_start_command = (f'django-admin startproject {projectTitle}')
os.system(django_start_command)

toolbar_width = 30

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar
print(f"Django project {projectTitle} created successfully :)")


set_up_app = input("What would you like to name your first app in your apps folder?")

create_apps = f"cd {projectTitle} && mkdir apps && cd apps && python3 ../manage.py startapp {set_up_app} && cd {set_up_app} && touch urls.py"
os.system(create_apps)
print(f"Creating Apps folder and adding {set_up_app} to Apps folder :)")

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar
print(f"Apps folder created and App: {set_up_app} added to apps folder and urls.py file added to: {set_up_app} :)")

print("Starting up Django server for you!")
django_server = f"Starting Django server for project {projectTitle}"

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar

print("Django server started running on Port 8000")
server = (f"cd {projectTitle} && python3 manage.py runserver")
os.system(server)




