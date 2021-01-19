from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
        

