from django.contrib import admin
from django.utils import timezone

from .models import Article, Comment


def publish_article(modeladmin, request, queryset):
    """Updates is_published and published_on fields of article object."""

    for article in queryset:
        article.is_published = True
        article.published_on = timezone.now()
        article.save()


def unpublish_article(modeladmin, request, queryset):
    """Updates is_published field of article object."""

    for article in queryset:
        article.is_published = False
        article.save()


def publish_comment(modeladmin, request, queryset):
    """Updates is_published field of a comment."""

    for comment in queryset:
        comment.is_published = True
        comment.save()


def unpublish_comment(modeladmin, request, queryset):
    """Updates is_published field of a comment."""

    for comment in queryset:
        comment.is_published = False
        comment.save()


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'is_published')
    list_editable = ('is_published', )
    list_filter = ('is_published', )
    search_fields = ('title', 'summary', 'content',)
    prepopulated_fields = {'slug': ('title', )}
    actions = (publish_article, unpublish_article)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('article', 'name', 'email', 'content', 'is_published')
    list_editable = ('is_published', )
    list_filter = ('is_published', )
    search_fields = ('article__title', 'name', 'email', 'content')
    actions = (publish_comment, unpublish_comment)