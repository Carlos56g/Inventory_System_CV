from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name="Product Name")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product_name} (Quantity: {self.quantity})"