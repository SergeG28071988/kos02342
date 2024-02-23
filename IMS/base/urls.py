from django.urls import path
from .import views

urlpatterns = [
    path('manufacturer_list/', views.manufacturer_list, name='manufacturer_list'),
    path('display_manufacturers/', views.display_manufacturers, name='display_manufacturers'),
    path('add_manufacturer/', views.add_manufacturer, name='add_manufacturer'),   

    path('product_list/', views.product_list, name='product_list'),
    path('display_laptops/', views.display_laptops, name='display_laptops'),
    path('add_laptop/', views.add_laptop, name='add_laptop'),

    path('display_desktops/', views.display_desktops, name='display_desktops'),
    path('add_desktop/', views.add_desktop, name='add_desktop'),

    path('display_mobiles/', views.display_mobiles, name='display_mobiles'),    
    path('add_mobile/', views.add_mobile, name='add_mobile'),    
]
