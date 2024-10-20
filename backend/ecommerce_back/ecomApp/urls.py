from django.urls import path
from ecomApp import views

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('products/', views.getProducts, name='getProducts'),
    path('product/<int:pk>/', views.get_product, name='getProduct')
]
