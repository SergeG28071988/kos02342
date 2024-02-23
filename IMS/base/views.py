from django.shortcuts import render, redirect, get_object_or_404
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
    


   

# def add_laptop(request):
#     # if request.method == 'POST':
#     #     form = LaptopForm(request.POST)

#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('product_list')
#     # else:
#     #     form = LaptopForm()
#     #     context = {
#     #         'form': form,
#     #         'header': 'Laptop'
#     #     }   
#     #     return render(request, 'add_new.html', context)   


# def add_desktop(request):
#     # if request.method == 'POST':
#     #     form = DesktopForm(request.POST)

#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('product_list')
#     # else:
#     #     form = DesktopForm()
#     #     context = {
#     #         'form': form,
#     #         'header': 'Desktop'
#     #     }   
#     #     return render(request, 'add_new.html', context) 


# def add_mobile(request):
#     # if request.method == 'POST':
#     #     form = MobileForm(request.POST)

#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('product_list')
#     # else:
#     #     form = MobileForm()
#     #     context = {
#     #         'form': form,
#     #         'header': 'Mobile'
#     #     }   
#     #     return render(request, 'add_new.html', context) 
    


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