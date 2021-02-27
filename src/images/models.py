from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m/%d')
    desciption = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    user_like = models.ManyToManyField(User, related_name='images_liked', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)