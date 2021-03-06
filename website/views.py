from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone as tz
import datetime
from django.db.models import Q


# Create your views here.


def index(request):

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip=get_ip(request)
    u=UserSession(user=ip)
    result = UserSession.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print("user exists")
    elif len(result) > 1:
        print("user exists again")

    else:
        u.save()
        print("user is uniqq")
    count = UserSession.objects.all().count()
    print("total users", count)

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
    checkOutCategory = Category.objects.all().order_by('?')[:3]
    compareTime = tz.now() - datetime.timedelta(days=6)
  

    new = False

    

    

    try:


          




        post = get_object_or_404(Post, slug=post_slug)
        
        post.view_count = post.view_count + 1
        post.save()

         
        

        if post.created >= compareTime:
            new = True
  
        
        
       
        
       
    except Exception as e:
        raise e

    return render(request, 'website/post.html', {'checkOutCategory':checkOutCategory,'post':post,'new':new, 'checkOutPost':checkOutPost})

   
