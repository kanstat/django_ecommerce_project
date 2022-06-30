from urllib import request
from django.shortcuts import render
from .models import *
# Create your views
#


def storee(request):
    context = {}
    data = Product.objects.all()
    context = {'data': data}
    return render(request, 'store/storee.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
