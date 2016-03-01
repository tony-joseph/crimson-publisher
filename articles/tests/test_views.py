from django.test import LiveServerTestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from selenium.webdriver.firefox.webdriver import WebDriver

from articles.models import Article, Comment


class ArticleViewsTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(ArticleViewsTestCase, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(ArticleViewsTestCase, cls).tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test1234')
        self.article_1 = Article.objects.create(
            author=self.user,
            title='test 1',
            slug='test-1',
            content='test 1',
            tags='tag-1, tag-2',
            category='test category',
        )
        self.article_2 = Article.objects.create(
            author=self.user,
            title='test 2',
            slug='test-2',
            content='test 2',
            tags='tag-1, tag-2',
            category='test category',
        )

    def test_article_list(self):
        self.selenium.get("{}{}".format(self.live_server_url, reverse('articles:article_list')))
        self.assertEqual("test 1" in self.selenium.page_source, True)
        self.assertEqual("test 2" in self.selenium.page_source, True)

    def test_article_view(self):
        self.selenium.get("{}{}".format(self.live_server_url, self.article_1.get_absolute_url()))
        self.assertEqual("test 1" in self.selenium.title, True)
        self.assertEqual("test 1" in self.selenium.page_source, True)
        self.assertEqual('tag-1' in self.selenium.page_source, True)
        self.assertEqual('tag-2' in self.selenium.page_source, True)

    def test_comments(self):
        client = Client()
        client.post("{}comments/".format(self.article_1.get_absolute_url()), {
            'name': 'test',
            'email': 'test@example.com',
            'content': 'This is a test comment'
        })
        self.assertEqual(Comment.objects.filter(email='test@example.com').exists(), True)
        Comment.objects.filter(email='test@example.com').update(is_published=True)
        self.selenium.get("{}{}comments".format(self.live_server_url, self.article_1.get_absolute_url()))
        self.assertEqual(self.article_1.title in self.selenium.title, True)
        self.assertEqual("This is a test comment" in self.selenium.page_source, True)

    def test_tag_view(self):
        self.selenium.get("{}{}".format(self.live_server_url, reverse('articles:article_list_by_tag',
                                                                      kwargs={'tag': 'tag-1'})))
        self.assertEqual("tag-1" in self.selenium.title, True)
        self.assertEqual("test 1" in self.selenium.page_source, True)
        self.assertEqual("test 2" in self.selenium.page_source, True)

    def test_category_view(self):
        self.selenium.get("{}{}".format(self.live_server_url, self.article_1.get_category_url()))
        self.assertEqual("test category" in self.selenium.title, True)
        self.assertEqual("test 1" in self.selenium.page_source, True)
        self.assertEqual("test 2" in self.selenium.page_source, True)

    def test_feeds(self):
        self.selenium.get("{}{}".format(self.live_server_url, reverse('articles:feed')))
        self.assertEqual("xml" in  self.selenium.page_source, True  )
