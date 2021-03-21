from rest_framework import serializers
from images.models import Image
from django.contrib.auth.models import User
from accounts.models import ExtendedUser

class MapUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = ('id', 'username')


class ImageSerializers(serializers.ModelSerializer):
    user_like = MapUserSerializers(many=True)
    class Meta:
        model = Image
        fields = ('title',
        'desciption',
        'image',
        'user_like',
        )