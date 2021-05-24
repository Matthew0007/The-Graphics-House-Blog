from .models import *



def menu(request):
    links = Category.objects.all()

    print(links[1].name)
    return dict(links=links)


def post_menu(request):

    post_list = Post.objects.all()
    return dict(post_list=post_list)

