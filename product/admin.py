from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
    'product_id', 'description', 'quantity_sum', 'cost_sum', 'sell_sum', 'profit_rupees', 'profit_percentage', 'day')
    list_filter = ['day']
    search_fields = ['product_id', 'description']


admin.site.register(Product, ProductAdmin)
