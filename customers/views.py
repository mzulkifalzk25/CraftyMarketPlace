from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Order, Customer
from django.views.generic import DetailView, TemplateView
from django.views import View


def cart_view(request):
    customer = request.user.customer
    cart = customer.cart
    context = {'cart': cart}

    return render(request, 'customers/cart.html', context)


def order_detail_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context = {'order': order}

    return render(request, 'customers/order_detail.html', context)


def customer_profile_view(request):
    customer = request.user.customer
    context = {'customer': customer}

    return render(request, 'customers/customer_profile.html', context)


def customer_profile_update(request):
    customer = request.user.customer

    return redirect('customers:customer_profile')
