from django.contrib import admin
from .models import *

# Register your models here.


class MessagsAdmin(admin.ModelAdmin):

    list_display = ('email', )
    

admin.site.register(Messages, MessagsAdmin)