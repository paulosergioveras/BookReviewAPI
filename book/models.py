from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    synopsis = models.TextField()
    genre = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    avg_rating = models.DecimalField(
        max_digits=3, decimal_places=1, default=0.0,
        validators=[
            MinValueValidator(0.0), MaxValueValidator(5.0)
        ])
    release_date = models.DateField()
    pages = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1)])
    publisher = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

