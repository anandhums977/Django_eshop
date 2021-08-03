from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.hashers import check_password
from store.models import Customer
from store.models import Product
from store.models import Order
from django.views import View



class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)


        for product in products:
            order = Order(customer = Customer(id = customer),
                          product = product,
                          price = product.price,
                          address = address,
                          phone = phone,
                          quantity = cart.get(str(product.id)))

            order.save()

        request.session['cart'] = {}
           

        return redirect('cart')