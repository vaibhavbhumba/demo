from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order

def Mazic(request):
    return render(request,'mazic.html')

def Story(request):
    return render(request,'story.html')

def Story2(request):
    return render(request,'story.html')
