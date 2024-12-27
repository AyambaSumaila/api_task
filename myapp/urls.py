from django.urls import path 
#from .views import ProductsListAPIView, ProductsDetailAPIView 

from .import views 

urlpatterns = [
     path('', views.ProductsListAPIView.as_view(), name='product_list'),
     path('<int:id>/', views.ProductsRetrieveAPIView.as_view(), name='product_detail'),
     path('create/', views.ProductsCreateAPIView.as_view(), name='product_create'),
     path('update/<int:id>/', views.ProductsRetrieveUpdateAPIView.as_view(), name="product_update"),
     path('delete/<int:id>/', views.ProductsDestroyAPIView.as_view(), name="product_delete"),

]

