from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):

    featured = Post.objects.filter(featured = True)

    return render(request, 'website/home.html', {'featured':featured})
