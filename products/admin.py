from django.contrib import admin
from .models import Product
from django.utils.html import format_html
from django.conf import settings

# Register your models here.
class customadmin(admin.ModelAdmin):
    list_display = ["id","product_name","company_name","image_tag","product_price"]
    list_filter = ["entered_by"]
    
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:100px; height:100px; border-radius:10%; object-fit:cover"/>',obj.product_image.url)


    

admin.site.register(Product,customadmin)



