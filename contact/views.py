from django.shortcuts import render
from django.http import HttpResponseRedirect
from contact.forms import *
from contact.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# Create your views here.




def submittedView(request):
    if request.method =='POST':
        formSubmitted = MessageForm(request.POST)
        if formSubmitted.is_valid():
            formSubmitted.save()
            return HttpResponseRedirect(reverse('website:home'))
    else:
        form = MessageForm()
        return HttpResponseRedirect(reverse('website:home'))

    








