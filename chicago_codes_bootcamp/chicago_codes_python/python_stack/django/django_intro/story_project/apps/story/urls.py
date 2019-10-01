from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^story$', views.story),
    url(r'^cop$', views.cop1),
    
]