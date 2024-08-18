from django.contrib import admin
from .models import Inventory_item, Category

admin.site.register(Inventory_item)
admin.site.register(Category)