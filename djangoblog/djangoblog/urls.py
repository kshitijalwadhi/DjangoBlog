from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^about/$', views.about),
    url('^$', article_views.article_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
