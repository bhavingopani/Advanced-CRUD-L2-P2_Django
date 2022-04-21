import django
from django.contrib import admin
from .models import User , Useraddress, Hobby, Userhobby


# Register your models here.

admin.site.register(User)
admin.site.register(Useraddress)
admin.site.register(Hobby)
admin.site.register(Userhobby)
