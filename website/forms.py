from django.forms import ModelForm
from .models import *




class PostForm(ModelForm):


    class Meta:
        model = Post
        fields = '__all__'


class CategoryForm(ModelForm):


    class Meta:
        model = Category
        fields = '__all__'