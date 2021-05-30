from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'slug')
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'created', 'category','image' )
    prepopulated_fields = {'slug':('title', )}

admin.site.register(Post, PostAdmin)



class UserAdmin(admin.ModelAdmin):
    list_display = ('user', )


    
    

admin.site.register(UserSession, UserAdmin)
