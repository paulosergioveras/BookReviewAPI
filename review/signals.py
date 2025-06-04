from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Review
from book.models import Book
from django.db.models import Avg


@receiver([post_save, post_delete], sender=Review)
def update_book_avg_rating(sender, instance, **kwargs):
    book = instance.book
    average = book.reviews.aggregate(avg=Avg('rating'))['avg'] or 0.0
    book.avg_rating = round(average, 1)
    book.save()
