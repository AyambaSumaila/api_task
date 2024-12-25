from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=3)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    created_by =models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name