from django.urls import path 
from .views import ProductsList, ProductsDetail 



urlpatterns = [
     path('', ProductsList.as_view(), name='products-list'),
     path('<int:pk>', ProductsDetail.as_view(), name='products-detail'),

]

