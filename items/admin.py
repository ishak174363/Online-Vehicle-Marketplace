from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('mode_name', 'price', 'stock',
                    'category', 'modified_date', 'is_available')

    prepopulated_fields = {'slug': ('mode_name',)}


admin.site.register(Product, ProductAdmin)
