from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^story$', views.story),
    url(r'^cop2$', views.cop2),
    url(r'^cop3$', views.cop3),
    url(r'^cop4$', views.cop4),
    url(r'^robber1$', views.robber1),
    url(r'^robber2$', views.robber2),
    url(r'^robber3$', views.robber3),
    url(r'^robber4$', views.robber4)

]