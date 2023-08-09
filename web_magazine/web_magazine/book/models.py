from django.core.exceptions import ValidationError
from django.db import models




# Create your models here.

def validate_max_size(cover):
    MAX_UPLOAD_SIZE = 5 * 1024 * 1024

    if cover.size > MAX_UPLOAD_SIZE:
        raise ValidationError("The book size must not exceed 5MB")



class Author(models.Model):
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
    )

    class Meta:
        unique_together = ('first_name', 'last_name')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(
        max_length=60,
    )

    description = models.TextField(
        max_length=650,
    )

    price = models.FloatField()

    cover = models.ImageField(
        upload_to='book_cover',
        validators=[validate_max_size,],


    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE,)



    def __str__(self):
        return f"{self.title}"



