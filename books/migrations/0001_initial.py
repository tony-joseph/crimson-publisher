# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 16:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('short_description', models.TextField()),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='books/book-featured-images/')),
                ('category', models.CharField(default='Uncategorised', max_length=256)),
                ('tags', models.CharField(blank=True, max_length=1024, null=True)),
                ('show_chapter_number', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_on',),
            },
        ),
        migrations.CreateModel(
            name='BookChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField()),
                ('chapter_number', models.PositiveIntegerField()),
                ('content', models.TextField()),
                ('summary', models.TextField(blank=True, null=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='books/book-chapter-featured-images/')),
                ('is_published', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
            options={
                'ordering': ('chapter_number',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='bookchapter',
            unique_together=set([('book', 'slug'), ('book', 'chapter_number')]),
        ),
    ]
