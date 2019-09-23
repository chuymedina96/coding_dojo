from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^goodbye$', views.goodbye),
    url(r'^signup$', views.signup),
    url(r'^login$', views.login),
    url(r'^new$', views.new)

]