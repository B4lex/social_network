from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, get_user_model
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

from accounts import forms
from accounts.models import FollowRelation


class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True


class UserRegisterView(CreateView):
    template_name = 'auth/register.html'
    form_class = forms.UserRegisterForm
    success_url = reverse_lazy('accounts:dashboard')

    def form_valid(self, form):
        return_value = super().form_valid(form)
        self.object.is_staff = True
        login(self.request, self.object, backend='django.contrib.auth.backends.ModelBackend')
        return return_value

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('accounts:dashboard'))
        else:
            return super().dispatch(request, *args, **kwargs)


class UserEditView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    form_class = forms.UserEditForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('accounts:dashboard')
    success_message = 'Changes successfully saved.'

    def get_object(self, queryset=None):
        return self.request.user


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'person_detail.html'
    context_object_name = 'person'


class UserListView(LoginRequiredMixin, ListView):
    template_name = 'people_list.html'
    context_object_name = 'people'
    model = get_user_model()
    queryset = model.objects.prefetch_related().all()

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(username__icontains=query) | Q(first_name__icontains=query) |
                Q(last_name__icontains=query) | Q(email__icontains=query)
            )
        return queryset


def follow_person(request):
    follow_to_id = request.POST.get('user_id')
    action = request.POST.get('action')
    failed = False

    user = get_user_model().objects.get(id=follow_to_id)
    if request.user != user:
        if action == 'follow' and user not in request.user.following.all():
            FollowRelation.objects.create(follower=request.user, follows_to=user)
        elif action == 'unfollow':
            try:
                FollowRelation.objects.get(follower=request.user, follows_to=user).delete()
            except FollowRelation.DoesNotExist:
                pass
        else:
            failed = True
    else:
        failed = True
    return JsonResponse({'status': 'ok' if not failed else 'fail'})
