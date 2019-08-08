from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=False)
    #blank=False -> the field must have value
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField(null=True) #null = True -> can have empty
    saleOrNot = models.BooleanField(null=True)

    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'id': self.id}) #f'/product/{self.id}/'

    def get_productList_url(self):
        return reverse('products:product-list')#f'/product/'