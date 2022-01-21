from .models import *
from contact.models import *
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import *
from django.db.models import Q
from contact.forms import *


def whatWeDo(request):
    whatWeDo = Post.objects.filter(category = 8)


    return dict(whatWeDo=whatWeDo)

def contribute(request):
    contribute = Post.objects.filter(category__name__contains="Contribute")
    
    


    return dict(contribute=contribute)


def menu(request):
    links = Category.objects.filter(navbar = True)

    
    return dict(links=links)

def user_count(request):
    def get_ip(request):
            address = request.META.get('HTTP_X_FORWARDED_FOR')
            if address:
                ip = address.split(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')
            return ip
            
    ip = get_ip(request)
    u = UserSession(user=ip)
    result = UserSession.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print("user exists")
    elif len(result) > 1:
        print("user exists again")

    else:
        u.save()
        print("user is uniqq")
    countusers = UserSession.objects.all().count()
    print("total users", countusers)       

    
    return dict(countusers=countusers)


def post_menu(request):

    post_list = Post.objects.filter(published = True)
    return dict(post_list=post_list)

def new_post(request):
    pass

def message_count(request):
    message_countAll = Messages.objects.filter(read=False)
    message_count = message_countAll.count()
    return dict(message_count=message_count)

def contact_form(request):

    formMessage = MessageForm()
    context = {

        'formMessage':formMessage
    }
    return context






