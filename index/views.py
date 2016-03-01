from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.gzip import gzip_page
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from articles.models import Article
from books.models import Book, BookChapter


class Index(View):

    @method_decorator(cache_page(60 * 15))
    @method_decorator(gzip_page)
    def get(self, request):
        category_list = set(Article.objects.order_by().values_list('category', flat=True))
        categories = []
        for c in category_list:
            categories.append({'name': c, 'slug': c.replace(' ', '-')})
        context = {
            'articles': Article.objects.filter(is_published=True, is_featured=True)[0:7],
            'books': Book.objects.filter(is_published=True)[0:5],
            'book_chapters': BookChapter.objects.filter(is_published=True).order_by('-created_on')[0:5],
            'categories': categories,
        }
        return render(request, 'index/index.html', context)
