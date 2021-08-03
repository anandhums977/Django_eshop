from django.shortcuts import render, render_to_response, redirect
from store.models import Product
from store.models import Category


def detail(request,id):
    product_object = Product.objects.get(id=id)
    return render(request,'detail.html',{'product_object':product_object}) 


