from django.test import TestCase
from django.contrib.auth.models import User

class FeedTest(TestCase):
    def setUp(self):
        User.objects.create_user('user4', email='email@email4', password='123qwe')
        User.objects.create_user('user2', email='email@email2', password='123qwe')
        User.objects.create_user('user3', email='email@email3', password='123qwe')
    
    def test_amount(self):
        users_quontity = User.objects.count()
        self.assertEqual(4,users_quontity )


