from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100, verbose_name="Nom")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

class Operation(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom")
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Description")
    amount = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Montant")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name= "Catégorie")
    date = models.DateField(verbose_name="Date")
    refunded = models.DateField(null=True, blank=True, verbose_name="Remboursement")

    def __str__(self) -> str:
        date = self.date.strftime("%d/%m/%Y")
        return f"{self.name} | {self.amount} € | {date}"
    
    @admin.display(description="Montant")
    def formated_amount(obj):
        if obj.amount > 0:
            color = "green"
            sign="+"
        elif obj.amount < 0:
            color = "red"
            sign=""
        else:
            color = "blue"
            sign=""
        return format_html(f'<strong><span style="color: {color};">{sign}{obj.amount} €</span></strong>')
    
    class Meta:
        verbose_name = "Opération"
        verbose_name_plural = "Opérations"
    
