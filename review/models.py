from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from book.models import Book




class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField(blank=True, null=True)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0,
        validators=[
            MinValueValidator(0.0), 
            MaxValueValidator(5.0)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
