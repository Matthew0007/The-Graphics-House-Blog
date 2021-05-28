from django.shortcuts import render
from django.db.models import Q
from website.models import *

# Create your views here.




def searchResults(request):
    posts = None
    query = None

    
    if 'q' in request.GET:
        query = request.GET.get('q')
        posts= Post.objects.all().filter(Q(title__contains=query))
    return render(request, 'search_app/search.html', {'query':query, 'posts':posts})


