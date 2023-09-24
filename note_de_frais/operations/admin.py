from django.contrib import admin
from .models import Operation
from .actions import mark_refunded

# Register your models here.

class OperationAdmin(admin.ModelAdmin):
    list_display = ("name", "amount", "date", "refunded")
    actions = [mark_refunded]

admin.site.register(Operation, OperationAdmin)