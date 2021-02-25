from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView


def test_view(request):
    return HttpResponse('HELLO')


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
