from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Article(models.Model):
    """ Model to store articles. """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    featured_image = models.ImageField(upload_to='articles/article-featured-images/', blank=True, null=True)
    category = models.CharField(max_length=256, default='Uncategorised')
    tags = models.CharField(max_length=1024, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=True)
    allow_comments = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-published_on',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article_view', kwargs={'slug': self.slug, })

    def get_comment_count(self):
        return Comment.objects.filter(article=self, is_published=True).count()

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',')] if self.tags else ''

    def get_category_url(self):
        return reverse('articles:article_list_by_category', kwargs={'category': str(self.category).replace(' ', '-')})


class Comment(models.Model):
    """ Model to store comments on an article. """

    article = models.ForeignKey(Article, db_index=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    content = models.TextField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=1024, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_on',)
