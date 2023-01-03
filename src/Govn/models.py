from django.db import models

# Create your models here.
class GOVN(models.Model):
    title  = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=6)
    new_field = models.BooleanField()