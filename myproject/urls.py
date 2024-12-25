
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/v1/', include('myapp.urls')),
    #user authentication
    path('api-auth/', include('rest_framework.urls')),
    
]
