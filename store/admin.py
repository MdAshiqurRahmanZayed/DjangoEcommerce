from django.contrib import admin
from .models import Product,Variation,ProductGallery,ReviewRating



# Register your models here.
class ProductAdmin(admin.ModelAdmin):
     list_display = ('product_name','price','stock','category','modified_at','is_available')
     prepopulated_fields = {
          'slug':('product_name',)
          }
     
class VariationsAdmin(admin.ModelAdmin):
     list_display = ('product', 'variation_category', 'variation_value', 'is_active')
     list_editable = ('is_active',)
     list_filter = ('product', 'variation_category', 'variation_value')
    


admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationsAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)

