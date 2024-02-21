from django.urls import path, include
from .views import manufacturer_list, product_list


urlpatterns = [
    path('manufacturer_list/', manufacturer_list, name='manufacturer_list'),
    path('product_list/', product_list, name='product_list'),
]
