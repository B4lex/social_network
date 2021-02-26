from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from .models import UserFeed
from django.contrib.auth.models import User
# Create your views here.
class FeedView(TemplateView):
    template_name = 'feed.html'

    def get_context_data(request, **kwargs):
        context = super().get_context_data(**kwargs)
        user_feed = UserFeed(User.objects.get(id=1))
        user_feed.get_feed_data()
        context['items'] = user_feed.data
        return context