from django.db import models

# Create your models here.

class Operation(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    refunded = models.DateField(null=True, blank=True)