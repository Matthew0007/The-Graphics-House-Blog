from django.shortcuts import render
from .models import *
from website.models import *
from website.forms import PostForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def main(request):
    context = {
    }
    return render(request,'dashboard/main.html', context)


def postsView(request):
    messages.success(request, "post added")
    post_listed = Post.objects.all()
    
    context = {
        'post_listed': post_listed,
    }
    return render(request, 'dashboard/posts.html', context)



def addPost(request):
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard:posts'))
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'dashboard/posts_add.html', context)


def editPost(request, category_slug, post_slug):
    editPost = Post.objects.get(category__slug=category_slug, slug=post_slug)
    form = PostForm(request.POST or None, request.FILES or None, instance = editPost)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('dashboard:posts'))
    context = {'form':form}
    return render(request, 'dashboard/posts_edit.html', context )


def deletePost(request, category_slug, post_slug):
    deletePost = Post.objects.get(category__slug=category_slug, slug=post_slug)
    if request.method == 'POST':      
        deletePost.delete()
        return HttpResponseRedirect(reverse('dashboard:posts'))
    
    return render(request, 'dashboard/posts_delete.html', {'deletePost':deletePost} )


def unpublishPost(request, category_slug, post_slug):
    unbpublish = Post.objects.get(category__slug=category_slug, slug=post_slug)
    saveData = unbpublish
    saveData.published = False
    saveData.save()
    return HttpResponseRedirect(reverse('dashboard:posts'))






