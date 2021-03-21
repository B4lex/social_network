from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


def get_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'profiles/{instance.username}.{ext}'


class ExtendedUser(AbstractUser):
    profile_image = models.ImageField(upload_to=get_image_upload_path, default='no_avatar.png', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    following = models.ManyToManyField(
        'self', through='accounts.FollowRelation', related_name='followers',
        null=True, blank=True, symmetrical=False
    )

    def __str__(self):
        return self.username


class FollowRelation(models.Model):
    follower = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, related_name='rel_from')
    follows_to = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, related_name='rel_to')
    followed_at = models.DateTimeField(auto_now_add=True)
