from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Main)
class MainTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'locations_title', 'locations','phonenumbers_title')


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('label', 'title', 'description')


@register(BestSeller)
class BestSellerTranslationOptions(TranslationOptions):
    fields = ('label', 'title', 'description')


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('label', 'title')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'ingredients',)


@register(RestaurantImages)
class RestaurantImagesTranslationOptions(TranslationOptions):
    fields = ('label',)


@register(Info)
class InfoTranslationOptions(TranslationOptions):
    fields = ('label', 'title', 'label_region', 'regions', 'label_schedule','label_phone')


@register(Days)
class DaysTranslationOptions(TranslationOptions):
    fields = ('day',)
