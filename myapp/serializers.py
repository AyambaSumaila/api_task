from rest_framework import serializers  # type: ignore

from .models import Products

class ProductsListSerializer(serializers.ModelSerializer):
   class Meta:
       model = Products
       fields = ('id', 'name', 'price', 'quantity', 'description', 'created_by')
       
       
       
class ProductsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'quantity', 'description', 'created_by')         
       
       
       
