import re

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

from web_magazine.accounts.models import Profile
from web_magazine.book.models import Book


# Create your models here.
def phone_regex_validator(value):
    if not re.match(r'^\+\d{1,15}$', value):
        raise ValidationError("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
# Create your models here.

class Cart(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



class Order(models.Model):
    CHOICES = (
        ('---','---'),
        ('In Progress','In Progress'),
        ('Pending','Pending'),
        ('Finished','Finished'),
    )


    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created =  models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=30,
        choices= CHOICES, default='Pending',
    )

    price = models.FloatField(
        default=0,
    )

    phone = models.CharField(
        max_length=17,
        validators=[phone_regex_validator, ],)



    address = models.TextField(
        max_length=58,
    )
