# myapp/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import produk_list, produk_create, produk_edit, produk_delete

urlpatterns = [
    path('', produk_list, name='produk_list'),
    path('produk/create/', produk_create, name='produk_create'),
    path('produk/edit/<int:pk>/', produk_edit, name='produk_edit'),
    path('produk/delete/<int:pk>/', produk_delete, name='produk_delete'),
]