from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.views.decorators.gzip import gzip_page
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.contrib import messages

from articles.models import Article, Comment
from articles.forms import CommentForm


class ArticleList(ListView):
    model = Article
    queryset = Article.objects.filter(is_published=True)
    template_name = 'articles/article-list.html'
    context_object_name = 'articles'
    paginate_by = 10

    @method_decorator(cache_page(60 * 15))
    @method_decorator(gzip_page)
    def dispatch(self, *args, **kwargs):
        return super(ArticleList, self).dispatch(*args, **kwargs)


class ArticleView(View):

    @method_decorator(cache_page(60 * 15))
    @method_decorator(gzip_page)
    def get(self,request, slug):
        article = get_object_or_404(Article, slug=slug)
        context = {
            'article': article,
            'form': CommentForm(),
        }
        return render(request, 'articles/article-view.html', context)


class CommentList(View):

    def get_object(self, slug):
        article = get_object_or_404(Article, slug=slug)
        return article

    def get_comments(self, article):
        return Comment.objects.filter(article=article, is_published=True)

    @method_decorator(cache_page(60 * 15))
    @method_decorator(gzip_page)
    def get(self, request, slug):
        article = self.get_object(slug=slug)
        context = {
            'article': article,
            'comments': self.get_comments(article=article),
            'form': CommentForm(),
        }
        return render(request, 'articles/comment-list.html', context)

    @method_decorator(gzip_page)
    def post(self, request, slug):
        article = self.get_object(slug=slug)
        user_agent = request.META.get('HTTP_USER_AGENT', None)
        ip_address = request.META.get('REMOTE_ADDR', None)
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            Comment.objects.create(
                article=article,
                name=name,
                email=email,
                content=content,
                user_agent=user_agent,
                ip_address=ip_address,
            )
            # Reload form to remove previous values
            form = CommentForm()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been submitted for verification.')
        else:
            messages.add_message(request, messages.ERROR, 'There are errors. Please correct.')

        context = {
            'article': article,
            'comments': self.get_comments(article),
            'form': form,
        }
        return render(request, 'articles/comment-list.html', context)


class ArticleListByTag(ListView):
    model = Article
    template_name = 'articles/article-list-by-tag.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(is_published=True, tags__icontains=self.kwargs['tag'])

    def get_context_data(self, **kwargs):
        context = super(ArticleListByTag, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context

    @method_decorator(cache_page(60 * 15))
    @method_decorator(gzip_page)
    def dispatch(self, *args, **kwargs):
        return super(ArticleListByTag, self).dispatch(*args, **kwargs)


class ArticleListByCategory(ListView):
    model = Article
    template_name = 'articles/article-list-by-category.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        category = self.kwargs['category'].replace('-', ' ')
        return Article.objects.filter(is_published=True, category=category)

    def get_context_data(self, **kwargs):
        context = super(ArticleListByCategory, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['category'].replace('-', ' ')
        return context

    @method_decorator(cache_page(60 * 15))
    @method_decorator(gzip_page)
    def dispatch(self, *args, **kwargs):
        return super(ArticleListByCategory, self).dispatch(*args, **kwargs)
