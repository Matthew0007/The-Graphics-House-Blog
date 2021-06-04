from django.urls import path 
from .views import signupView, signinView, signoutView
from website import views


urlpatterns = [

    path('create/', signupView, name='signup'),
    path('login/', signinView, name='signin'),
    path('logout/', signupView, name='signout'),


]