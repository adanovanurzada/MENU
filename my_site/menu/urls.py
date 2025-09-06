from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register(r'main', MainViewSet, basename='main')
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'about', AboutUsViewSet, basename='about')
router.register(r'bestseller-images', BestSellerImagesViewSet, basename='bestseller-images')
router.register(r'bestsellers', BestSellerViewSet, basename='bestsellers')
router.register(r'menu', MenuViewSet, basename='menu')
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'products-images', ProductsImageViewSet, basename='products-images')
router.register(r'images', ImagesViewSet, basename='images')
router.register(r'restaurant-images', RestaurantImagesViewSet, basename='restaurant-images')
router.register(r'days', DaysViewSet, basename='days')
router.register(r'schedules', ScheduleViewSet, basename='schedules')
router.register(r'info', InfoViewSet, basename='info')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
]
