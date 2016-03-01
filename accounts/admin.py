from django.contrib import admin
from django.contrib.auth.models import User

from .models import UserProfile


admin.site.unregister(User)


class UserProfileInline(admin.StackedInline):
    model = UserProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    inlines = [UserProfileInline, ]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'gender')
