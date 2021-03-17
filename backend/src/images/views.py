from rest_framework import viewsets
from images.models import Image
from images.serializers import ImageSerializers

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers