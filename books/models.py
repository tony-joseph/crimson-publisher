from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Book(models.Model):
    """ Model to store book data."""

    title = models.CharField(max_length=512)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField()
    short_description = models.TextField()
    featured_image = models.ImageField(upload_to='books/book-featured-images/', blank=True, null=True)
    category = models.CharField(max_length=256, default='Uncategorised')
    tags = models.CharField(max_length=1024, blank=True, null=True)
    show_chapter_number = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_view', kwargs={'slug': self.slug})

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',')]


class BookChapter(models.Model):
    """ Model to store book chapters. """

    book = models.ForeignKey(Book, db_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    slug = models.SlugField(db_index=True)
    chapter_number = models.PositiveIntegerField()
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    featured_image = models.ImageField(upload_to='books/book-chapter-featured-images/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('chapter_number',)
        unique_together = (
            ('book', 'chapter_number'),
            ('book', 'slug'),
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_chapter_view', kwargs={'book_slug': self.book.slug, 'chapter_slug': self.slug})

    def get_next_chapter(self):
        try:
            return BookChapter.objects.get(book=self.book, chapter_number=self.chapter_number+1)
        except self.DoesNotExist:
            return None

    def get_previous_chapter(self):
        try:
            return BookChapter.objects.get(book=self.book, chapter_number=self.chapter_number-1)
        except self.DoesNotExist:
            return None
