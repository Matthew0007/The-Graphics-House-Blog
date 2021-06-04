from django.db import models

# Create your models here.


class Messages(models.Model):
    name = models.CharField(max_length=128)
    body = models.TextField()
    email = models.EmailField(null=False)
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.name
