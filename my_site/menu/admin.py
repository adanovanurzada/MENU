from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin



class ProductsImageInline(admin.TabularInline):
    model = ProductsImage
    extra = 1


@admin.register(Products)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductsImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Main)
admin.site.register(Contact)
admin.site.register(AboutUs)
admin.site.register(BestSeller)
admin.site.register(BestSellerImages)
admin.site.register(Menu)
admin.site.register(RestaurantImages)
admin.site.register(Images)
admin.site.register(Info)
admin.site.register(Days)
admin.site.register(Schedule)