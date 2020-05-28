from django.contrib import admin
from .models import Item
# from the current directory models folder, import the class
# Register your models here.


admin.site.register(Item)
