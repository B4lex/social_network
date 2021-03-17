from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from server import settings
import os


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m/%d')
    desciption = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.user_like.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])

    def delete(self, *args, **kwargs):
        os.remove(f'{settings.MEDIA_ROOT}{self.image}')
        super().delete(*args, **kwargs)