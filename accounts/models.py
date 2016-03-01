from django.db import models

from django.contrib.auth.models import User


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Not specified', 'Not specified')
)


class UserProfile(models.Model):
    """ Model to store the user profile.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, blank=True, default='Not specified', choices=GENDER_CHOICES)
    about = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    home_page = models.CharField(max_length=256, blank=True, null=True)
    twitter = models.CharField(max_length=256, blank=True, null=True)
    facebook = models.CharField(max_length=256, blank=True, null=True)
    google_plus = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=128, blank=True, null=True)
    state = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
