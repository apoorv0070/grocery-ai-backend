from django.db import models
from stores.models import Store
class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    def __str__(self): return self.name
