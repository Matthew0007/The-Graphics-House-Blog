from django.shortcuts import render
from .models import *
from website.models import *
from website.forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


# ==================================================DASHBOARD======================================================

def main(request):
    context = {
    }
    return render(request,'dashboard/main.html', context)

# ==================================================POSTS======================================================
def postsView(request):
    messages.success(request, "post added")
    posts_unordered = Post.objects.all()
    post_listed = posts_unordered.order_by('-created')
    
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


def publishPost(request, category_slug, post_slug):
    publish = Post.objects.get(category__slug=category_slug, slug=post_slug)
    saveData = publish
    saveData.published = True
    saveData.save()
    return HttpResponseRedirect(reverse('dashboard:posts'))

# ==================================================Category======================================================

def categoryView(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return render(request, 'dashboard/category.html', context)


def editCategory(request, category_slug):
    editCateogry = Category.objects.get(slug=category_slug)
    form = CategoryForm(request.POST or None, instance = editCateogry)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('dashboard:categories'))
    context = {'form':form}
    return render(request, 'dashboard/category_edit.html', context )


def deleteCategory(request, category_slug):
    deleteCategory = Category.objects.get(slug=category_slug)
    posts_category = Post.objects.filter(category__slug = category_slug)
    if request.method == 'POST':      
        deleteCategory.delete()
        return HttpResponseRedirect(reverse('dashboard:categories'))
    
    return render(request, 'dashboard/category_delete.html',{'deleteCategory':deleteCategory, 'posts_category':posts_category} )



def addCategory(request):
    if request.method =='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard:categories'))
    else:
        form = CategoryForm()
    context = {
        'form':form,
    }
    return render(request, 'dashboard/category_add.html', context)