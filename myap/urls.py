from django.urls import path, include
# from .models import Product
# from rest_framework.routers import DefaultRouter
from .views import ListProduct,DetailProduct
from .views import ProductView
from . import views

# router = DefaultRouter()
# router.register(r'product', ProductView)

urlpatterns = [
    path('products/',ListProduct.as_view(), name = 'product'),
    path('products/<int:pk>',DetailProduct.as_view(), name = 'newproduct'),
    path('api/product/', ProductView.as_view(), name='product'),
    path('buyer/<int:buyer_id>/', views.buyer_detail, name='buyer_detail'),

]


