from django.contrib import admin
from .models import BlogPost
from .models import Catagory
# Register your models here.

admin.site.register(Catagory)
admin.site.register(BlogPost)