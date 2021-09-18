from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from website.models import *

# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    profile_image = models.ImageField(upload_to='accounts', blank=False, default='accounts/user01.jpeg')

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'email'
    ]
    
class Author(models.Model):
    profile_image = models.ImageField(upload_to='accounts', blank=False, default='accounts/user01.jpeg')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    about = RichTextUploadingField()


    def countPosts(self):
        count = 0
        for post in Post.objects.all():
            if post.author == self.user:
                count = count+1
                
        return count




