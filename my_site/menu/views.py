from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class MainViewSet(viewsets.ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializers


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializers


class BestSellerImagesViewSet(viewsets.ModelViewSet):
    queryset = BestSellerImages.objects.all()
    serializer_class = BestSellerSerializers


class BestSellerViewSet(viewsets.ModelViewSet):
    queryset = BestSeller.objects.all()
    serializer_class = BestSellerSerializers



class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['category_name']


class CategoryDetailAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'ingredients']



class ProductsImageViewSet(viewsets.ModelViewSet):
    queryset = ProductsImage.objects.all()
    serializer_class = ProductsImageSerializers


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class RestaurantImagesViewSet(viewsets.ModelViewSet):
    queryset = RestaurantImages.objects.all()
    serializer_class = RestaurantImagesSerializer\


class DaysViewSet(viewsets.ModelViewSet):
    queryset = Days.objects.all()
    serializer_class = DaysSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
