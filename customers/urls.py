from django.urls import path
from . import views


app_name = 'customers'


urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('order/<int:pk>/', views.order_detail_view, name='order_detail'),
    path('profile/', views.customer_profile_view, name='customer_profile'),
    path('profile/update/', views.customer_profile_update,
         name='customer_profile_update'),
]
