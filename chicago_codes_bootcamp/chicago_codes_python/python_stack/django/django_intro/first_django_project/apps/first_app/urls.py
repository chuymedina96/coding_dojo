from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup$', views.sign),
    url(r'login', views.login),
    url(r'^goodbye$', views.goodbye)
]