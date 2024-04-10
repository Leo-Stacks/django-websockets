from django.db import models
import uuid
# Create your models here.
class Product(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    price = models.FloatField()