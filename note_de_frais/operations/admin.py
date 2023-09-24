from django.contrib import admin
from .models import Operation

# Register your models here.

class OperationAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "date", "refunded")

admin.site.register(Operation, OperationAdmin)