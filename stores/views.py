from ctypes import addressof
from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
from . utils import cookieCart, cartData, guestOrder
import datetime
from django.views.generic import DetailView
import json
from .models import *

def stores(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'stores/stores.html', context)

# Creating the list of each post
class PostDetailView(DetailView):
    model = Product
    template_name = 'stores/product_details.html'

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
        
                   
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'stores/cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'stores/checkout.html', context)

# setting up the javascript view
def updateItem(request):
    data = json.loads(request.body)
    productId  = data['productId']
    action = data['action']
    print ('Action:', action )
    print('ProductId:', productId)

    # add the Customer
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product= product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
         orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was aded', safe=False)


def processOrder(request):
    # print('Data:', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)  #getting data

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)


    else:
        customer, order = guestOrder(request, order)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    # preventing user from malipulating from the frontend
    if total == float(order.get_cart_total):
        order.complete = True
        order.save()

    # setting the value of shipping
    if order.shipping == True:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )
    return JsonResponse('Payment Subbmitted', safe=False)