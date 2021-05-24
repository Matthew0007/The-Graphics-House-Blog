from django.contrib import admin
from .models import Category, Post
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'slug')
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'created', 'category', )
    prepopulated_fields = {'slug':('title', )}

admin.site.register(Post, PostAdmin)
