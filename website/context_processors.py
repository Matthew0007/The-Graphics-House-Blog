from .models import *
from contact.models import *
from contact.models import *
from contact.forms import *

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






