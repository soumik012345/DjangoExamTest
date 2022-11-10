from django.contrib import admin

# Register product model here.
from .models import Product, ProductImage, ProductVariant, ProductVariantPrice, Variant

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantPrice)
admin.site.register(Variant)