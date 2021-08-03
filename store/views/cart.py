from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.hashers import check_password
from store.models import Customer
from store.models import Product
from django.views import View
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator



class Cart(View):

    @method_decorator(auth_middleware)
    def get(self,request):
        ids =  list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
       
        print('ids',products)
        return render(request,'cart.html', {'products':products})
  