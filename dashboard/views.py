from django.shortcuts import render
from .models import *
from website.models import *
from website.forms import *
from accounts.models import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib import messages
from contact.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def group_check(user):
    if user.groups.filter(name="Admin").exists() == True:
        return True
    else:
        return False

# ==================================================DASHBOARD======================================================
@user_passes_test(group_check)
def main(request):

    userVisited = UserSession.objects.order_by().values('user').distinct().count()
    print(userVisited)
    allPosts = Post.objects.all()
    highest = allPosts.order_by('-view_count')
    highest = highest[0]
    print(highest.view_count)
        

    
    context = {
        'visitedTotal':userVisited,
        'highest':highest.view_count
    }
    return render(request,'dashboard/main.html', context)

# ==================================================POSTS======================================================
@user_passes_test(group_check)
def postsView(request):
    messages.success(request, "post added")
    posts_unordered = Post.objects.all()
    post_listed = posts_unordered.order_by('-created')


    paginator = Paginator(post_listed, 9)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        posted = paginator.page(page)
    except  (EmptyPage, InvalidPage):
        posted = paginator.page(paginator.num_pages)


    
    context = {
        'post_listed': post_listed,
        'posted': posted    }
    return render(request, 'dashboard/posts.html', context)


@user_passes_test(group_check)
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

@user_passes_test(group_check)
def editPost(request, category_slug, post_slug):
    editPost = Post.objects.get(category__slug=category_slug, slug=post_slug)
    form = PostForm(request.POST or None, request.FILES or None, instance = editPost)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('dashboard:posts'))
    context = {'form':form}
    return render(request, 'dashboard/posts_edit.html', context )

@user_passes_test(group_check)
def deletePost(request, category_slug, post_slug):
    deletePost = Post.objects.get(category__slug=category_slug, slug=post_slug)
    if request.method == 'POST':      
        deletePost.delete()
        return HttpResponseRedirect(reverse('dashboard:posts'))
    
    return render(request, 'dashboard/posts_delete.html', {'deletePost':deletePost} )

@user_passes_test(group_check)
def unpublishPost(request, category_slug, post_slug):
    unbpublish = Post.objects.get(category__slug=category_slug, slug=post_slug)
    saveData = unbpublish
    saveData.published = False
    saveData.save()
    return HttpResponseRedirect(reverse('dashboard:posts'))

@user_passes_test(group_check)
def publishPost(request, category_slug, post_slug):
    publish = Post.objects.get(category__slug=category_slug, slug=post_slug)
    saveData = publish
    saveData.published = True
    saveData.save()
    return HttpResponseRedirect(reverse('dashboard:posts'))

# ==================================================Category======================================================
@user_passes_test(group_check)
def categoryView(request):
    category_list = Category.objects.all()


    context = {
        'category_list': category_list,
    }
    return render(request, 'dashboard/category.html', context)

@user_passes_test(group_check)
def editCategory(request, category_slug):
    editCateogry = Category.objects.get(slug=category_slug)
    form = CategoryForm(request.POST or None, instance = editCateogry)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('dashboard:categories'))
    context = {'form':form}
    return render(request, 'dashboard/category_edit.html', context )

@user_passes_test(group_check)
def deleteCategory(request, category_slug):
    deleteCategory = Category.objects.get(slug=category_slug)
    posts_category = Post.objects.filter(category__slug = category_slug)
    if request.method == 'POST':      
        deleteCategory.delete()
        return HttpResponseRedirect(reverse('dashboard:categories'))
    
    return render(request, 'dashboard/category_delete.html',{'deleteCategory':deleteCategory, 'posts_category':posts_category} )


@user_passes_test(group_check)
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




    # ==================================================Authors======================================================

@user_passes_test(group_check)
def AuthorView(request):
    author_list = Author.objects.all()
    context = {
        'author_list': author_list,
    }
    return render(request, 'dashboard/author.html', context)



      # ==================================================Authors======================================================

@user_passes_test(group_check)
def messageView(request):
    cacheRead = []
    message_list = Messages.objects.all().order_by('-created')
    for message in message_list:
        obj = get_object_or_404(Messages, id=message.id)
        if obj.read == False:
            cacheRead.append(obj.id)
        obj.read=True
        
        obj.save()
    context = {
        'message_list': message_list,
        'cacheRead':cacheRead
    }
    return render(request, 'dashboard/message.html', context)