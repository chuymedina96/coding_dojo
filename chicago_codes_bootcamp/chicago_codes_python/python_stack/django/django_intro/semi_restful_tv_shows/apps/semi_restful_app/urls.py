from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^shows/new$', views.index),
    url(r'^shows$', views.shows),
    url(r'^shows/create$', views.createShow),
    url(r'^shows/(?P<show_id>\d+)$', views.viewShow),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.editShow),
    url(r'^shows/(?P<show_id>\d+)/update$', views.updateShow),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.destroyShow)

]