from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from images.tests.factories.user import UserFactory
from images.tests.factories.image import ImageFactory, Image

from io import BytesIO
from PIL import Image as Pil
from django.core.files.base import File
from unittest.mock import Mock



class ImageViewTestCase(TestCase):
    PASSWORD = UserFactory.get_password()

    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.login = self.client.login(username=self.user, password=self.PASSWORD)
        count = 1
        while count < 10:
            ImageFactory(user=self.user)
            count += 1

    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Pil.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def testLogin(self):
        self.assertTrue(self.login)

    def test_image_list(self):
        response = self.client.get('/images', follow=True)
        Image.objects.filter(user_id=self.user)
        self.assertEqual(response.status_code, 200)
        images = Image.objects.filter(user_id=2)
        [self.assertIn(i.title, response.content) for i in images]

    def test_image_create(self):
        create_image = self.get_image_file(name='1.png')
        response = self.client.get('/images/create', follow=True)
        response_1 = self.client.post('/images/create/',
                                      {'title': '10', 'desciption': '10', 'image': create_image})
        response_2 = self.client.post('/images/create/',
                                      {'title': '', 'desciption': '10', 'image': create_image})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_1)
        self.assertTrue(response_2)

    def test_image_update(self):
        create_image = self.get_image_file(name='1.png')
        image_1 = Image.objects.get(id=1)
        response = self.client.get('/images/update/1')
        self.assertIn(image_1.title, str(response.content))
        self.assertIn(image_1.desciption, str(response.content))
        self.client.post('/images/update/1', {'title': '10', 'desciption': '10', 'image': create_image})
        self.assertNotEqual(image_1.title, Image.objects.get(id=1).title)

    def test_image_delete(self):
        self.client.get('/images/delete/2')
        self.client.post('/images/delete/2')

    def test_image_detail(self):
        image = Image.objects.get(id=1)
        response = self.client.get(f'/images/detail/{image.id}/{image.slug}')
        self.assertIn(image.title, str(response.content))
        self.assertIn(image.desciption, str(response.content))
        self.assertIn(image.image.url, str(response.content))

    def test_image_like_and_unlike(self):
        image = Image.objects.get(id=4).total_likes
        self.assertEqual(image, 0)
        self.client.post('/images/like/',
                         {'action': 'like', 'id': 4},
                         **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(Image.objects.get(id=4).total_likes, 1)
        response = self.client.post('/images/like/',
                                    {'action': 'unlike', 'id': 4},
                                    **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.content, b'{"status": "ok"}')
        response = self.client.post('/images/like/',
                                    {'action': 'unlike', 'id': 'exept'},
                                    **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(response.content, b'{"status": "error"}')
        response = self.client.post('/images/like/',
                         {'action': 'unlike', 'id': 'exept'})
        self.assertEqual(response.status_code, 400)

