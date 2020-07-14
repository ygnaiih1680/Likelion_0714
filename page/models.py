from django.db import models


# Create your models here.
class Contents(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
