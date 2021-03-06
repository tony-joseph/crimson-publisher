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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Not specified', 'Not specified')], default='Not specified', max_length=30)),
                ('about', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('home_page', models.CharField(blank=True, max_length=256, null=True)),
                ('twitter', models.CharField(blank=True, max_length=256, null=True)),
                ('facebook', models.CharField(blank=True, max_length=256, null=True)),
                ('google_plus', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('state', models.CharField(blank=True, max_length=128, null=True)),
                ('country', models.CharField(blank=True, max_length=128, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
