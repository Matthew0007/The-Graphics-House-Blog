from .models import *


def whatWeDo(request):
    whatWeDo = Post.objects.filter(category = 8)


    return dict(whatWeDo=whatWeDo)


def menu(request):
    links = Category.objects.filter(navbar = True)

    
    return dict(links=links)


def post_menu(request):

    post_list = Post.objects.filter(published = True)
    return dict(post_list=post_list)

def new_post(request):
    pass

