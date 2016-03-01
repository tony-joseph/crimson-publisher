from django.conf.urls import url

from articles.feeds import ArticleFeed
from . import views


urlpatterns = [
    url(r'^profiles/(?P<username>[-a-zA-Z0-9_]+)/$', views.UserProfileView.as_view(), name='user_profile_view'),
]