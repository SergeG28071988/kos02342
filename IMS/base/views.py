from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .models import *
from .forms import *

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


def add_manufacturer(request):
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('manufacturer_list')
    else:
        form = ManufacturerForm()
        context = {
            'form': form,
            'header': 'Manufacturer'
        }   
        return render(request, 'add_manufacturer.html', context)    
    


def manufacturer_detail(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)

    context = {
        'manufacturer': manufacturer,
    }

    return render(request, 'manufacturer_detail.html', context)
       


def add_product(request, cls, header):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect("product_list")
        
    else:
        form = cls()
        
        context = {
            'form': form,            
            'header': header,            
        }   
        return render(request, 'add_new.html', context)


def add_laptop(request):
    return add_product(request, LaptopForm, 'Add Laptop')

def add_desktop(request):
    return add_product(request, DesktopForm, 'Add Desktop')

def add_mobile(request):
    return add_product(request, MobileForm, 'Add Mobile')


def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    return render(request, 'laptop_detail.html', {'item': laptop})

def desktop_detail(request, pk):
    desktop = get_object_or_404(Desktop, pk=pk)
    return render(request, 'desktop_detail.html', {'item': desktop})

def mobile_detail(request, pk):
    mobile = get_object_or_404(Mobile, pk=pk)
    return render(request, 'mobile_detail.html', {'item': mobile})