from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'pot_size',
        'height',
        'image',
    )

    ordering = ('sku',)

admin.site.register(Product, ProductAdmin)