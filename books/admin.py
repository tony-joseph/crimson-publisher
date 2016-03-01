from django.contrib import admin

from .models import Book, BookChapter


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'is_published')
    list_editable = ('is_published', )
    list_filter = ('is_published', )
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug': ('title', )}


@admin.register(BookChapter)
class BookChapterAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'book', 'is_published')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'book')
    search_fields = ('title', 'summary', 'content',)
    prepopulated_fields = {'slug': ('title', )}
