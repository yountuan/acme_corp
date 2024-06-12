from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'price', 'category', 'in_stock']
    search_fields = ['name', 'description', 'price', 'category', 'in_stock']
    ordering_fields = ['price']
    pagination_class = CustomPageNumberPagination

    def __str__(self):
        return self.name