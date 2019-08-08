from django.contrib import admin

# Register your models here.
# from the current models.py import Product Class.
from .models import Product

admin.site.register(Product)