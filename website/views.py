from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.


def index(request):

    whatWeDo = Post.objects.filter(category = 8)

    featured = Post.objects.filter(featured = True)

    for i in whatWeDo:
       pass

    return render(request, 'website/home.html', {'featured':featured, 'whatWeDo':whatWeDo})


def allPostCat(request, category_slug):

    if request.user.groups.filter(name="Manager").exists() == True:
        managerCheck = True

    cat = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(category=cat, published=True) 
   
    return render(request, 'website/category.html', {'category':cat,'posts':posts })


def post_detail(request, category_slug, post_slug):

    try:
        post = get_object_or_404(Post, slug=post_slug)
        post.view_count = post.view_count +1
        post.save()
    except Exception as e:
        raise e

    return render(request, 'website/post.html', {'post':post})

   
