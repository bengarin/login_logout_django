from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name    
        
