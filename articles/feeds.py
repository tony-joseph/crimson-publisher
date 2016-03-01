from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

from articles.models import Article
from publisher.config import SITE_CONFIG


class ArticleFeed(Feed):
    """ RSS 2 feed for all published articles. """

    title = "{} {}".format(SITE_CONFIG['SITE_NAME'], SITE_CONFIG['ARTICLE_NAME_PLURAL'])
    link = '/articles/feed/'
    description = "Latest {} from {}".format(SITE_CONFIG['ARTICLE_NAME_PLURAL'], SITE_CONFIG['SITE_NAME'])

    def items(self):
        return Article.objects.filter(is_published=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary if item.summary else item.content[:200]
