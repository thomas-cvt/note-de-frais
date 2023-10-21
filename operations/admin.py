from django.contrib import admin
from .models import Operation, Category
from .actions import mark_refunded

# Register your models here.

class OperationAdmin(admin.ModelAdmin):
    list_display = ("name", "formated_amount", "date", "refunded")
    actions = [mark_refunded]
    list_filter = [("refunded", admin.EmptyFieldListFilter)]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ["name",]

admin.site.register(Operation, OperationAdmin)
admin.site.register(Category, CategoryAdmin)