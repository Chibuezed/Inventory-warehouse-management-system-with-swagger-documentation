from django.shortcuts import render

# Create your views here.

# inventory/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Category, Supplier, Product, StockMovement
from .serializers import (
    CategorySerializer, SupplierSerializer, ProductSerializer, StockMovementSerializer
)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StockMovementViewSet(ModelViewSet):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
