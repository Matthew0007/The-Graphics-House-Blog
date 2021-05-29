from django.shortcuts import render
from .models import *
from website.models import *

# Create your views here.


def main(request):


    return render(request,'dashboard/main.html', {})
