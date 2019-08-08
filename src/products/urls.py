from django.urls import path
from .views import (
    product_detail_view, 
    product_create_view, 
    product_raw_view, 
    product_lookup_view
    )

app_name = 'products'
urlpatterns = [
    path('', product_detail_view, name='product-list'),
    path('<int:id>/', product_lookup_view, name='product-detail'),
    path('create/', product_create_view, name='product-create'),
    path('raw/', product_raw_view, name='product-raw'),
]