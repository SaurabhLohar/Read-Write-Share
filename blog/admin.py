from django.contrib import admin
from .models import Post,Profile
# Register your models here.
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.register(Post)

admin.site.register(Profile)