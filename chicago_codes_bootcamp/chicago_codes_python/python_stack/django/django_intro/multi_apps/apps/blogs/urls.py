from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.getBlog),
    url(r'^(?P<number>\d+)/edit$', views.editBlog),
    url(r'^(?P<number>\d+)/delete$', views.destroy)

]

#   url(r'^(?P<my_var>\w+)$', views.greet)