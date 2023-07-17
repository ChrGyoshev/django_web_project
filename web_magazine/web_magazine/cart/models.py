from django.core.validators import RegexValidator
from django.db import models


from web_magazine.accounts.models import Profile
from web_magazine.book.models import Book


# Create your models here.

phone_regex = RegexValidator(regex=r'^\+\d{1,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class Cart(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

