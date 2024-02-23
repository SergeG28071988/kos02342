from django.urls import path, include
from .views import manufacturer_list, product_list, display_manufacturers, display_laptops, display_desktops, display_mobiles


urlpatterns = [
    path('manufacturer_list/', manufacturer_list, name='manufacturer_list'),
    path('display_manufacturers/', display_manufacturers, name='display_manufacturers'),
    path('product_list/', product_list, name='product_list'),
    path('display_laptops/',display_laptops, name='display_laptops'),
    path('display_desktops/', display_desktops, name='display_desktops'),
    path('display_mobiles/', display_mobiles, name='display_mobiles'),    
]
