from django.db import models

# Create your models here.
class Pppages(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=3, max_digits=6)
    summary = models.CharField(max_length=50)