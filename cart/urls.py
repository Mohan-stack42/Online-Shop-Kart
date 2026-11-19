# cart/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:pk>/<str:action>/', views.update_quantity, name='update_quantity'),
]