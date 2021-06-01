from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.main, name='main'),
    path('posts/', views.postsView, name='posts'),
    path('PostAdd/', views.addPost, name='addPost'),
    path('PostEdit/<slug:category_slug>/<slug:post_slug>/', views.editPost, name='editPost'),
    path('PostDelete/<slug:category_slug>/<slug:post_slug>/', views.deletePost, name='deletePost'),
    path('UnpublishPost/<slug:category_slug>/<slug:post_slug>/', views.unpublishPost, name='unpublishPost'),


   
    
]