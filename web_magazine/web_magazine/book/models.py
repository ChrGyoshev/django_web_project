from django.db import models




# Create your models here.


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
        max_length=30,
    )

    description = models.TextField(
        max_length=150,
    )

    price = models.FloatField()

    cover = models.ImageField(
        upload_to='book_cover'
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE,)

    def __str__(self):
        return f"{self.title}"


