from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.views.decorators.gzip import gzip_page
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import Book, BookChapter


class BookList(ListView):
    model = Book
    queryset = Book.objects.filter(is_published=True)
    template_name = 'books/book-list.html'
    context_object_name = 'books'
    paginate_by = 10

    @method_decorator(cache_page(60 * 15))
    @method_decorator(gzip_page)
    def dispatch(self, *args, **kwargs):
        return super(BookList, self).dispatch(*args, **kwargs)


class BookView(View):

    def get_object(self, slug):
        return get_object_or_404(Book, slug=slug, is_published=True)

    @method_decorator(cache_page(60 * 15))
    @method_decorator(gzip_page)
    def get(self, request, slug):
        book = self.get_object(slug=slug)
        book_chapters = BookChapter.objects.filter(book=book, is_published=True)
        context = {
            'book': book,
            'book_chapters': book_chapters,
        }
        return render(request, 'books/book-view.html', context)


class BookChapterView(View):

    @method_decorator(cache_page(60 * 15))
    @method_decorator(gzip_page)
    def get(self, request, book_slug, chapter_slug):
        book = get_object_or_404(Book, slug=book_slug, is_published=True)
        chapter = get_object_or_404(BookChapter, book=book, slug=chapter_slug, is_published=True)
        all_chapters = BookChapter.objects.filter(book=book, is_published=True)
        context = {
            'book': book,
            'chapter': chapter,
            'all_chapters': all_chapters,
        }
        return render(request, 'books/book-chapter-view.html', context)
