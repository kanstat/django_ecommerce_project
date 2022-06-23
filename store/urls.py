from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.storee, name='storee'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
