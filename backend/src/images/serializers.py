from rest_framework import serializers
from images.models import Image

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('title',
         'desciption',
          'image',
           'user_like',
            'total_likes')