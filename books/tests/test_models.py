from django.test import TestCase
from django.contrib.auth.models import User

from books.models import Book, BookChapter


class BookTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test1234')

    def test_book_create_update_delete(self):
        Book.objects.create(
            title='test',
            author=self.user,
            slug='test',
            description='test book description',
            short_description='short description',
        )
        self.assertEqual(Book.objects.filter(slug='test').exists(), True)

        Book.objects.filter(slug='test').update(slug='test1')
        self.assertEqual(Book.objects.filter(slug='test1').exists(), True)
        self.assertEqual(Book.objects.filter(slug='test').exists(), False)

        Book.objects.filter(slug='test1').delete()
        self.assertEqual(Book.objects.filter(slug='test1').exists(), False)


class BookChapterTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test1234')
        self.book = Book.objects.create(
            title='test',
            author=self.user,
            slug='test',
            description='test book description',
            short_description='short description',
        )

    def test_book_create_update_delete(self):
        BookChapter.objects.create(
            book=self.book,
            title='test',
            slug='test',
            chapter_number=1,
            content='test book chapter description',
            summary='short description',
        )
        self.assertEqual(BookChapter.objects.filter(slug='test').exists(), True)

        BookChapter.objects.filter(slug='test').update(slug='test1')
        self.assertEqual(BookChapter.objects.filter(slug='test1').exists(), True)
        self.assertEqual(BookChapter.objects.filter(slug='test').exists(), False)

        BookChapter.objects.filter(slug='test1').delete()
        self.assertEqual(BookChapter.objects.filter(slug='test1').exists(), False)
