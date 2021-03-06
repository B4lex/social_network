from images.models import Image
import factory, factory.django
from images.tests.factories.user import UserFactory, User
from django.shortcuts import get_object_or_404


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image
        django_get_or_create = ('user_id', 'title', 'image', 'desciption')

    user_id = 1
    title = factory.Sequence(lambda n: 'Image %d' % n)
    image = factory.django.ImageField(color='blue')
    desciption = factory.Sequence(lambda n: 'Company %d' % n)