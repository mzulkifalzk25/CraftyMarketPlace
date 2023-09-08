from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Admin
from customers.models import Order
from django.views.generic import DetailView, TemplateView, ListView
from django.views import View
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Check if the user is an admin


def is_admin(user):
    return user.is_superuser


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(user_passes_test(is_admin, login_url='login'), name='dispatch')
class AdminDashboardView(TemplateView):
    template_name = 'admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_products'] = Product.objects.count()
        context['total_orders'] = Order.objects.count()
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(user_passes_test(is_admin, login_url='login'), name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'admin/product_list.html'
    context_object_name = 'products'


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(user_passes_test(is_admin, login_url='login'), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'admin/product_detail.html'
    context_object_name = 'product'

# Add more admin views for orders, customers, etc., as needed
