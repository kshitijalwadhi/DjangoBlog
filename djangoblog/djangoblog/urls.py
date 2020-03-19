from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^about/$', views.about),
    url('^$', views.homepage),
]
