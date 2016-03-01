"""publisher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static

from articles import urls as articles_urls
from books import urls as books_urls
from accounts import urls as accounts_urls
from index import views as index_views

urlpatterns = [
    url(r'^$', index_views.Index.as_view(), name='index'),

    url(r'^admin/', admin.site.urls),

    url(r'^articles/', include(articles_urls, namespace='articles')),

    url(r'^books/', include(books_urls, namespace='books')),

    url(r'^accounts/', include(accounts_urls, namespace='accounts')),

    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
]
