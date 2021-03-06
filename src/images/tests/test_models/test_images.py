from images.models import Image
from django.shortcuts import get_object_or_404
from server import settings

from io import BytesIO
from PIL import Image as Pil
from django.core.files.base import File
import os.path

from django.test import TestCase
from django.test.client import Client

from images.tests.factories.user import UserFactory
from images.tests.factories.image import ImageFactory


class ImageModelsTestCase(TestCase):

    PASSWORD = UserFactory.get_password()

    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.login = self.client.login(username=self.user, password=self.PASSWORD)
        count = 1
        while count < 10:
            ImageFactory(user=self.user)
            count += 1

    def testLogin(self):
        self.assertTrue(self.login)

    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Pil.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def test_models_images(self):
        UserFactory()
        image = Image(
            user_id=1,
            title='Phone',
            image=self.get_image_file('1'),
            desciption='HelloWord!')
        image.save()
        image = get_object_or_404(Image, id=1)
        self.assertEqual(str(image), image.title)
        self.assertTrue(image.slug)
        self.assertEqual(image.total_likes, 0)
        self.assertEqual(image.get_absolute_url(), f'/images/detail/{image.id}/{image.slug}')
        image.delete()
        self.assertEqual(os.path.exists(f'{settings.MEDIA_ROOT}{image.image}'), False)