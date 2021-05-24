from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:category_slug>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/', views.allPostCat, name='category_detail'),
    
]