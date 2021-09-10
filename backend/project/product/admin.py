from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from product.models import Category, Product, Shop, ProductState

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(ProductState)
