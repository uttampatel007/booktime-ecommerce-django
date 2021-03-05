from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=40)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	slug = models.SlugField(max_length=50)
	active = models.BooleanField(default=True)
	in_stock = models.BooleanField(default=True)
	date_updated = models.DateTimeField(auto_now=True)


class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="product-images")