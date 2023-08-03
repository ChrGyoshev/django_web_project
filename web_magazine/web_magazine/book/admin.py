from django.contrib import admin


from web_magazine.book.models import Book, Author


# Register your models here.
@admin.register(Author)
class BookAuthor(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'price','author',
    ]
    search_fields = [
        'price','title', 'author__first_name', 'author__last_name',
    ]

    ordering = ['-price']

    list_filter = ['title','price',]

