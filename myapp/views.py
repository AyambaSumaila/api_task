from .models import  Products
from django.shortcuts import render
from rest_framework import generics, permissions 
from.models import Products 
from.serializers import ProductsListSerializer, ProductsDetailSerializer #


class ProductsListAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializer
    
    
    #Retrieve view 
class ProductsRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializer    
    
    #Create product view 
class ProductsCreateAPIView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializer        
    
    


#Product retrieve update view     
class ProductsRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field='id'
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializer   
    
    #Delete view 
class ProductsDestroyAPIView(generics.DestroyAPIView):
    lookup_field='id'
    queryset = Products.objects.all()
    
    
    
