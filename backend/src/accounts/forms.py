from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("username", 'first_name', 'email')


class UserEditForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ("username", 'first_name', 'last_name', 'email', 'profile_image', 'birth_date')


class UserSearchForm(forms.Form):
    search_field = forms.CharField()
