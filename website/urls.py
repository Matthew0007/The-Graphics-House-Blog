from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
    path('', views.index, name='home'),
    path('<slug:slug>', views.index, name='category_detail'),
    
]