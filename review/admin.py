from django.contrib import admin
from .models import Review




@admin.register(Review)
class ModelAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'book',
        'comment',
        'rating',
        'created_at',
        'updated_at'
    )