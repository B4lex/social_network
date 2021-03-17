from django.contrib import admin
from images.models import Image

# Create your views here.

@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'desciption')
