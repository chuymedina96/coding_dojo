from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^wall$', views.success),
    url(r'^logout$', views.logout),
    url(r'^login$', views.login),
    url(r'^newmessage$', views.newMessage),
    url(r'^newcomment$', views.createComment)

]