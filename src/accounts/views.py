from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from accounts import forms


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = forms.UserRegisterForm
    success_url = reverse_lazy('accounts:dashboard')

    def form_valid(self, form):
        return_value = super().form_valid(form)
        self.object.is_staff = True
        self.object.profile.create()
        login(self.request, self.object)
        return return_value

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('accounts:dashboard'))
        else:
            return super().dispatch(request, *args, **kwargs)


class UserEditView(SuccessMessageMixin, UpdateView):
    form_class = forms.UserEditForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('accounts:dashboard')
    success_message = 'Changes successfully saved.'
    profile_form = forms.ProfileEditForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['profile_form'] = self.profile_form(instance=self.object.profile)
        return context_data

    def post(self, request, *args, **kwargs):
        profile_form = self.profile_form(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if profile_form.is_valid():
            profile_form.save()
            return super().post(request, *args, **kwargs)
        else:
            return super().form_invalid(self.get_form())


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
