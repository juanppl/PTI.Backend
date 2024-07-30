from django.contrib import admin
from categories.models import Category
from products.models import Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)