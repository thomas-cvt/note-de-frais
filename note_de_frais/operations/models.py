from django.db import models

# Create your models here.

class Operation(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom")
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Description")
    amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Montant")
    category = models.CharField(max_length=100, null=True, blank=True, verbose_name= "Catégorie")
    date = models.DateField(verbose_name="Date")
    refunded = models.DateField(null=True, blank=True, verbose_name="Remboursement")

    def __str__(self) -> str:
        date = self.date.strftime("%d/%m/%Y")
        return f"{self.name} | {self.amount} | {date}"