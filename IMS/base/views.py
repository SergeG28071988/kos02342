from django.shortcuts import render

# Create your views here.

def manufacturer_list(request):
    return render(request, 'manufacturer_list.html')


def product_list(request):
    return render(request, 'product_list.html')