from django.forms import ModelForm
from .models import *




class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'body']