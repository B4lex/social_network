from django.shortcuts import render, HttpResponse
from django.views.generic.base import TemplateView
from .feed_classes import UserFeed
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class FeedView(LoginRequiredMixin, TemplateView):
    template_name = 'feed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_feed = UserFeed(user = self.request.user)
        if(user_feed.get_feed_data()):
            context['type'] = 'user_feed'
        else:
            context['type'] = 'recent_feed'
        if hasattr(user_feed, 'data'):
            context['items'] = user_feed.data
        else:
            context['items'] = []
        return context