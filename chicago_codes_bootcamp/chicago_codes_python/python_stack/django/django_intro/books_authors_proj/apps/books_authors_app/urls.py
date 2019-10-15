from django.conf.urls import url
from . import views
from .models import *

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.authors),
    url(r'^add_book$', views.newBook),
    url(r'^add_author$', views.newAuthor),
    url(r'^authors/(?P<author_id>\d+)$', views.viewAuthors),
    url(r'^books/(?P<book_id>\d+)$', views.viewBook),
    url(r'^add_author_to_book$', views.addAuthorToBook),
    url(r'^add_book_to_author$', views.addBookToAuthor),
]
