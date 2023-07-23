from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

from web_magazine.accounts.models import Profile
from web_magazine.book.models import Book


# Create your models here.


class Cart(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



class Order(models.Model):
    CHOICES = (
        ('In Progress','In Progress'),
        ('Pending','Pending'),
    )


    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created =  models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=30,
        choices= CHOICES, default='Pending',
    )




