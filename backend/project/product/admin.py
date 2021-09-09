from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from product.models import Category

admin.site.register(Category, MPTTModelAdmin)
