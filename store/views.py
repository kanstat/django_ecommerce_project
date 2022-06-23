from urllib import request
from django.shortcuts import render

# Create your views
#


def storee(request):
    context = {}
    return render(request, 'store/storee.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
