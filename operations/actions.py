from datetime import datetime
from django.contrib import admin

@admin.action(description="Marquer comme remboursé")
def mark_refunded(modeladmin, request, queryset):
    queryset.update(refunded=datetime.now())