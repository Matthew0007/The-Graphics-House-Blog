from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', 'profile_image', 'first_name', 'last_name']


    

admin.site.register(CustomUser, CustomUserAdmin)



class AuthorAdmin(admin.ModelAdmin):

    list_display = ('user', 'first_name', )



    
admin.site.register(Author, AuthorAdmin)