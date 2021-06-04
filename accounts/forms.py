from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import *


class CustomUserCreationForm(UserCreationForm):


    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields +('profile_image','first_name','last_name',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class AuthorForm(ModelForm):


    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'user', 'profile_image']