from django.contrib import admin
from .models import Category,Subcategory,Product

# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity','subcategory')
admin.site.register(Product , AdminProduct)
admin.site.register(Category)    
admin.site.register(Subcategory)    
        
