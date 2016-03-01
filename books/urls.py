from django.conf.urls import url

from articles.feeds import ArticleFeed
from . import views


urlpatterns = [
    url(r'^$', views.BookList.as_view(), name='book_list'),

    url(r'^(?P<slug>[-a-zA-Z0-9_]+)/$', views.BookView.as_view(), name='book_view'),

    url(r'^(?P<book_slug>[-a-zA-Z0-9_]+)/(?P<chapter_slug>[-a-zA-Z0-9_]+)/$', views.BookChapterView.as_view(),
        name='book_chapter_view'),
]