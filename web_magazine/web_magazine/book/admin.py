from django.contrib import admin


from web_magazine.book.models import Book, Author


# Register your models here.
@admin.register(Author)
class BookAuthor(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
    ]
    search_fields = [
        'first_name', 'last_name'
    ]
    ordering = ['first_name']

    list_filter = ['first_name']

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

