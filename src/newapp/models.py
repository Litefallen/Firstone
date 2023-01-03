from django.db import models

# Create your models here.
class Mewapp(models.Model):
    title       = models.CharField(max_length=50)
