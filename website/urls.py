from django.urls import path
from . import views


app_name = 'webiste'

urlpatterns = [
    path('', views.index, name='home'),
    
]