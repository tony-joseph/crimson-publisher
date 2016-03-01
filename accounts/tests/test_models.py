from django.test import TestCase
from django.contrib.auth.models import User

from accounts.models import UserProfile


class UserTestCase(TestCase):

    def test_user_profile_creation_on_user_creation(self):
        user = User.objects.create_user(username='test', password='test1234')
        self.assertEqual(UserProfile.objects.filter(user=user).exists(), True)
