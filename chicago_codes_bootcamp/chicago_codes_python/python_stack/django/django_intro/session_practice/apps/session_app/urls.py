from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^destroy$', views.destroy_session),
    url(r'^add_two$', views.add_two)

]