from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from selenium.webdriver.firefox.webdriver import WebDriver

from books.models import Book, BookChapter


class BookViewsTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(BookViewsTestCase, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(BookViewsTestCase, cls).tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test1234')
        self.book_1 = Book.objects.create(
            title='test 1',
            author=self.user,
            slug='test1',
            description='test book 1 description',
            short_description='short description 1',
        )
        self.book_2 = Book.objects.create(
            title='test 2',
            author=self.user,
            slug='test2',
            description='test book 2 description',
            short_description='short description 2',
        )
        self.chapter_1 = BookChapter.objects.create(
            book=self.book_1,
            title='chapter 1',
            slug='chapter-1',
            chapter_number=1,
            content='this is chapter 1'
        )
        self.chapter_2 = BookChapter.objects.create(
            book=self.book_1,
            title='chapter 2',
            slug='chapter-2',
            chapter_number=2,
            content='this is chapter 2'
        )

    def test_book_list(self):
        self.selenium.get("{}{}".format(self.live_server_url, reverse('books:book_list')))
        self.assertEqual("test 1" in self.selenium.page_source, True)
        self.assertEqual("test 2" in self.selenium.page_source, True)

    def test_book_view(self):
        self.selenium.get("{}{}".format(self.live_server_url, self.book_1.get_absolute_url()))
        self.assertEqual("test 1" in self.selenium.title, True)
        self.assertEqual("test 1" in self.selenium.page_source, True)
        self.assertEqual("chapter 1" in self.selenium.page_source, True)
        self.assertEqual("chapter 2" in self.selenium.page_source, True)

    def test_book_chapter_view(self):
        self.selenium.get("{}{}".format(self.live_server_url, self.chapter_1.get_absolute_url()))
        self.assertEqual("chapter 1" in self.selenium.title, True)
        self.assertEqual("chapter 1" in self.selenium.page_source, True)
        self.assertEqual("this is chapter 1" in self.selenium.page_source, True)
