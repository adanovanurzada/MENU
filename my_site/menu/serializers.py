from  rest_framework import  serializers
from .models import  *


class MainSerializers(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['id','restaurant_name','title','description','locations_title','locations','phonenumbers_title','phonenumbers','image']


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['label_name', 'image_name' , 'name', 'label_phone', 'image_phone', 'phone']

class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields  = ['label', 'title', 'description', 'image_one', 'image_two']


class BestSellerImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = BestSellerImages
        fields = ['id', 'image']


class BestSellerSerializers(serializers.ModelSerializer):
    best_seller = BestSellerImageSerializers(many=True, read_only=True)
    class Meta:
        model = BestSeller
        fields = ['id', 'label', 'title', 'description', 'best_seller']


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','label','title']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class ProductsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsImage
        fields = ['id','image']


class ProductsSerializers(serializers.ModelSerializer):
    images_product = ProductsImageSerializers(many=True, read_only=True)
    class Meta:
        model = Products
        fields = ['id','description','title','ingredients','price','images_product']


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id','restaurant_images']


class RestaurantImagesSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    class Meta:
        model = RestaurantImages
        fields = '__all__'


class DaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = ['id', 'day']


class ScheduleSerializer(serializers.ModelSerializer):
    start_day = DaysSerializer()
    end_day = DaysSerializer()
    start_time = serializers.TimeField(format='%H:%M')
    end_time = serializers.TimeField(format='%H:%M')
    class Meta:
        model = Schedule
        fields = ['id', 'start_time', 'end_time', 'start_day', 'end_day']


class CategoryDetailSerializer(serializers.ModelSerializer):
    products_category = ProductsSerializers(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'products_category']


class InfoSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Info
        fields = ['id', 'label', 'title', 'title_region', 'regions', 'label_schedule',
                  'label_phone','phone', 'email','schedule']