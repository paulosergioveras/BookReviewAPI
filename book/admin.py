from django.contrib import admin
from .models import Book




@admin.register(Book)
class ModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'synopsis',
        'genre',
        'isbn',
        'avg_rating',
        'release_date',
        'pages',
        'publisher',
        'created_at'
    )