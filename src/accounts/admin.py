from django.contrib import admin

from accounts.models import ExtendedUser, FollowRelation


@admin.register(ExtendedUser)
class ExtendedUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


@admin.register(FollowRelation)
class FollowRelationAdmin(admin.ModelAdmin):
    list_display = ('follower', 'follows_to', 'followed_at')
