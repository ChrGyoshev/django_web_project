from django.contrib import admin


from web_magazine.book.models import Book, Author


# Register your models here.
@admin.register(Author)
class BookAuthor(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

