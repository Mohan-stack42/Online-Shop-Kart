# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('bill/<int:pk>/', views.bill, name='bill'),
    path('my-orders/', views.my_orders, name='my_orders'),
]