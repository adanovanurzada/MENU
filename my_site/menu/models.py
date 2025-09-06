from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Main(models.Model):
    restaurant_name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    locations_title = models.CharField(max_length=64)
    locations = models.CharField(max_length=127)
    image = models.ImageField(upload_to='main_images/')
    phonenumbers_title = models.CharField(max_length=64)
    phonenumbers = PhoneNumberField(region='KG')

    def __str__(self):
        return f'{self.restaurant_name}'


class Contact(models.Model):
    label_name = models.CharField(max_length=27)
    image_name = models.ImageField(upload_to='name_image/')
    name = models.CharField(max_length=32)
    label_phone = models.CharField(max_length=27)
    image_phone = models.ImageField(upload_to='phone_image/')
    phone = PhoneNumberField(region='KG', unique=True)


    def __str__(self):
        return f'{self.name}'

class AboutUs(models.Model):
    label = models.CharField(max_length=27)
    title = models.CharField(max_length=127)
    description = models.TextField()
    image_one = models.ImageField(upload_to='images_one/')
    image_two = models.ImageField(upload_to='images_two/')

    def __str__(self):
        return f'{self.label}'


class BestSeller(models.Model):
    label = models.CharField(max_length=27)
    title = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return f'{self.label}'


class BestSellerImages(models.Model):
    image = models.ImageField(upload_to='bestseller_images/')
    best_seller = models.ForeignKey(BestSeller, on_delete=models.CASCADE, related_name='best_photos')

    def __str__(self):
        return f'{self.best_seller}'

class Menu(models.Model):
    label = models.CharField(max_length=27)
    title = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.label}'

class Category(models.Model):
    category_name = models.CharField(max_length=27)

    def __str__(self):
        return f'{self.category_name}'

class Products(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    ingredients = models.TextField()
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE,related_name='menu_products')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products_category')

    def __str__(self):
        return f'{self.title}'

class ProductsImage(models.Model):
    image = models.ImageField(upload_to='products_image')
    products_images = models.ForeignKey(Products,on_delete=models.CASCADE,related_name='images_product')


    def __str__(self):
        return f'{self.products_images}'


class RestaurantImages(models.Model):
    label = models.CharField(max_length=27)


    def __str__(self):
        return f'{self.label}'

class Images(models.Model):
    image = models.ImageField(upload_to='restaurant_images/')
    restaurant_images = models.ForeignKey(RestaurantImages, on_delete=models.CASCADE, related_name='imagess')

    def __str__(self):
        return f'{self.restaurant_images}'


class Info(models.Model):
    label = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    label_region = models.CharField(max_length=128)
    title_region = models.CharField(max_length=255)
    regions = models.CharField(max_length=127)
    label_schedule = models.CharField(max_length=27)
    label_phone = models.CharField(max_length=27)
    phone = PhoneNumberField(region='KG')
    email = models.EmailField(unique=True)



    def __str__(self):
        return f'{self.label}'



class Days(models.Model):
    day = models.CharField(max_length=27)

    def __str__(self):
        return f'{self.day}'


class Schedule(models.Model):
    start_time = models.TimeField()
    the_end_time = models.TimeField()
    start_day = models.ForeignKey(Days, on_delete=models.CASCADE, related_name='day_start')
    the_end_day = models.ForeignKey(Days, on_delete=models.CASCADE, related_name='day_end')
    restaurant = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='schedule')

    def __str__(self):
        return f'{self.restaurant}'

