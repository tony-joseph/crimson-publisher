from django.conf.urls import url

from articles.feeds import ArticleFeed
from . import views


urlpatterns = [
    url(r'^$', views.ArticleList.as_view(), name='article_list'),

    url(r'^tag/(?P<tag>[-a-zA-Z0-9_]+)/$', views.ArticleListByTag.as_view(), name='article_list_by_tag'),

    url(r'^category/(?P<category>[-a-zA-Z0-9_]+)/$', views.ArticleListByCategory.as_view(),
        name='article_list_by_category'),

    url(r'^feed/$', ArticleFeed(), name='feed'),

    url(r'^(?P<slug>[-a-zA-Z0-9_]+)/$', views.ArticleView.as_view(), name='article_view'),

    url(r'^(?P<slug>[-a-zA-Z0-9_]+)/comments/$', views.CommentList.as_view(), name='comment_list'),
]