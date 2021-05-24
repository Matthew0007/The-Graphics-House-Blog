from .models import *


def whatWeDo(request):
    whatWeDo = Post.objects.filter(category = 8)


    return dict(whatWeDo=whatWeDo)


def menu(request):
    links = Category.objects.all()

    print(links[1].name)
    return dict(links=links)


def post_menu(request):

    post_list = Post.objects.all()
    return dict(post_list=post_list)

