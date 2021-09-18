from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone as tz
import datetime
from django_ip_geolocation.decorators import with_ip_geolocation

# Create your views here.


def index(request):

    whatWeDo = Post.objects.filter(category = 8)
    featured = Post.objects.filter(featured = True)
    for i in whatWeDo:
       pass
    # print(request.geolocation['continent'])
    return render(request, 'website/home.html', {'featured':featured, 'whatWeDo':whatWeDo})


def allAuthorCat(request, category_slug):
    if request.user.groups.filter(name="Manager").exists() == True:
        managerCheck = True
    cat = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=cat, published=True) 
    return render(request, 'website/category.html', {'category':cat,'posts':posts })



def allPostCat(request, category_slug):
    if request.user.groups.filter(name="Manager").exists() == True:
        managerCheck = True
    cat = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=cat, published=True) 
    return render(request, 'website/category.html', {'category':cat,'posts':posts })


    
def post_detail(request, category_slug, post_slug):
    checkOutPost = Post.objects.all().order_by('?')[:3]
    compareTime = tz.now() - datetime.timedelta(days=6)
  

    new = False

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    try:
        post = get_object_or_404(Post, slug=post_slug)
        

        if post.created >= compareTime:
            new = True
  
        ip= get_ip(request)
        result = UserSession.objects.filter(user=ip, post=post)
        u = UserSession(user=ip, post=post)
        if result:
            print("hello")
        else:
            print("nah")
            u.save()
            post.view_count = post.view_count + 1
            post.save()
       
    except Exception as e:
        raise e

    return render(request, 'website/post.html', {'post':post,'new':new, 'checkOutPost':checkOutPost})

   
