from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Artisan, Product, CustomOrder, Review


def artisan_list(request):
    artisans = Artisan.objects.all()
    context = {'artisans': artisans}
    return render(request, 'artisans/artisan_list.html', context)


def artisan_detail(request, pk):
    artisan = get_object_or_404(Artisan, pk=pk)
    context = {'artisan': artisan}
    return render(request, 'artisans/artisan_detail.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'artisans/product_detail.html', context)
