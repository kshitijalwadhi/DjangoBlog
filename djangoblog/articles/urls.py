from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    url('^$', views.article_list, name="list"),
    url('^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
