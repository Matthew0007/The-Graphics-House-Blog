from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from accounts.forms import *



# Create your views here.

def signoutView(request):
    logout(request)
    return redirect('signup')

def signupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            signup_user = CustomUser.objects.get(username = username)
            staff_group = Group.objects.get(name='Staff')
            added = staff_group.user_set.add(signup_user)
            
            obj = Author.objects.create(
                profile_image = signup_user.profile_image,
                user = signup_user,
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name']


            )
            obj.save()
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form':form})


def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('website:home')
            else:
                return redirect('signup')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form':form})
