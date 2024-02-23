from django.shortcuts import render
from .models import *

# Create your views here.

def manufacturer_list(request):
    return render(request, 'manufacturer_list.html')


def product_list(request):
    return render(request, 'product_list.html')


def display_manufacturers(request):
    manufacturers = Manufacturer.objects.all()

    context = {
        'manufacturers': manufacturers,
        'header': 'Manufacturer' 
    }   
    
    return render(request, 'manufacturer_list.html', context)


def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header': 'Laptop'
    }   
    
    return render(request, 'product_list.html', context)
    

def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header': 'Desktop'
    }   
    
    return render(request, 'product_list.html', context)


def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header': 'Mobile'
    }   
    
    return render(request, 'product_list.html', context)
