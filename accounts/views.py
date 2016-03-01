from hashlib import md5

from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User

from accounts.models import UserProfile


class UserProfileView(View):

    def get_object(self, username):
        return get_object_or_404(User, username=username, is_active=True)

    def get(self, request, username):
        user = self.get_object(username)
        context = {
            'user': user,
            'user_profile': get_object_or_404(UserProfile, user=user),
            'gravathar_hash': md5(user.email.encode()).hexdigest()
        }
        return render(request, 'accounts/user-profile-view.html', context)
