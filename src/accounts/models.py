from django.db import models
from django.contrib.auth import get_user_model


def get_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'profiles/{instance.user.username}.{ext}'


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
