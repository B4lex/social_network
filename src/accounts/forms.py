from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from accounts.models import Profile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("username", 'first_name', 'email')


class UserEditForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ("username", 'first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('profile_image', 'birth_date')

