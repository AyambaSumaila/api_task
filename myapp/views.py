from .models import  Products
# Create your views here.
from django.shortcuts import render
from rest_framework import generics, permissions 
from.models import Products 
from.serializers import ProductsSerializer
# Create your views here.


class ProductsList(generics.ListCreateAPIView):
   #For authenticated users   
    #permission_classes = [permissions.IsAuthenticated] 
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    
    
class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
   # permission_classes = [permissions.IsAuthenticated]  
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer    
    
    
    