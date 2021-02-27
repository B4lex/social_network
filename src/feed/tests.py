from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from .models import Action, Post, Contact
from .utils import create_action
from .views import FeedView
from unittest.mock import patch
from .feed_classes import UserFeed


class FeedTest(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        user4 = User.objects.create_user('user4', email='email@email4', password='123qwe')
        create_action(user4, "created")
        user2 = User.objects.create_user('user2', email='email@email2', password='123qwe')
        create_action(user2, "created")
        user3 = User.objects.create_user('user3', email='email@email3', password='123qwe')
        create_action(user3, "created")
        user1 = User.objects.create_user('user1', email='email@email1', password='123qwe1')
        create_action(user1, "created")
        post1 = Post(user = user1,image_url="url",description="description")
        post1.save()
        create_action(user1, "posted", post1) 
        post2 = Post(user = user2,image_url="url",description="description")
        post2.save()
        create_action(user2, "posted", post2) 
        cnt1 = Contact(user_from = user1, user_to = user2)
        cnt1.save()

        self.factory = RequestFactory()
        self.user = user1

    def test_not_dublicating_aactions(self):
        user1 = User.objects.get(id=4)
        user2 = User.objects.get(id=2)
        pre_count = Action.objects.count()
        create_action(user1, "posted", Post.objects.get(id=1))
        count = Action.objects.count()
        self.assertEqual(pre_count, count)

        create_action(user1, 'followed', user2)
        pre_count = Action.objects.count()
        self.assertEqual(pre_count-1, count)
        
        create_action(user1, 'followed', user2) 
        count = Action.objects.count()
        self.assertEqual(pre_count, count)

    def test_view_context(self):
        request = self.factory.get('/feed/dashboard')
        request.user = self.user
        view = FeedView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('items', context)
        self.assertEqual(len(context['items']),2)
        self.assertEqual(context['type'], 'user_feed')

    def test_no_data_in_feed(self):
        request = self.factory.get('/feed/dashboard')
        request.user = User.objects.get(id=1)
        view = FeedView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('items', context)
        self.assertEqual(context['type'], 'recent_feed')

    def test_with_mock(self):
        with patch.object(UserFeed, 'get_popular_posts', return_value=None) as mock_method:
            request = self.factory.get('/feed/dashboard')
            request.user = User.objects.get(id=1)
            view = FeedView()
            view.setup(request)

            context = view.get_context_data()
        assert mock_method.called