from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^logout$', views.logout),
    url(r'^process_message$', views.process_message),
    url(r'^process_comment$', views.process_comment),
    url(r'^messages/(?P<message_id>\d+)/delete$', views.delete_message),
    url(r'^comments/(?P<comment_id>\d+)/delete$', views.delete_comment),
    url(r'^messages/(?P<message_id>\d+)/like$', views.like_message),
    url(r'^messages/(?P<message_id>\d+)/unlike$', views.unlike_message),
    url(r'^comments/(?P<comment_id>\d+)/like$', views.like_comment),
    url(r'^comments/(?P<comment_id>\d+)/unlike$', views.unlike_comment),
]