from django.urls import path

from web_magazine.book.views import BookCatalogue, AddBook

urlpatterns = [
    path('catalogue/', BookCatalogue.as_view(),name='book catalogue' ),
    path('add-book/',AddBook.as_view(),name='add book'),


]


