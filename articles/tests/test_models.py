from django.test import TestCase
from django.contrib.auth.models import User

from articles.models import Article, Comment


class ArticleTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test1234')
        Article.objects.create(
            author=self.user,
            title='test article',
            slug='test',
            content='test article'
        )

    def test_article_create(self):
        Article.objects.create(
            author=self.user,
            title='test article 1',
            slug='test-1',
            content='test article one'
        )
        self.assertEqual(Article.objects.filter(slug='test-1').exists(), True)

    def test_article_update(self):
        article = Article.objects.get(slug='test')
        article.slug = 'test-2'
        article.save()
        self.assertEqual(Article.objects.filter(slug='test').exists(), False)
        self.assertEqual(Article.objects.filter(slug='test-2').exists(), True)

    def test_article_delete(self):
        article = Article.objects.get(slug='test')
        article.delete()
        self.assertEqual(Article.objects.filter(slug='test').exists(), False)
