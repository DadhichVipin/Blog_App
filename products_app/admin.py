from django.contrib import admin
from products_app.models import Products


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']


admin.site.register(Products, AdminProduct)

