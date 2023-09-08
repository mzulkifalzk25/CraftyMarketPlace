from django.urls import path
from . import views


app_name = 'artisans'


urlpatterns = [
    path('list/', views.artisan_list, name='artisan_list'),
    path('detail/<int:pk>/', views.artisan_detail, name='artisan_detail'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
