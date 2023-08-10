from django.urls import path

from web_magazine.book.views import BookCatalogue, AddBook, BookDetails

urlpatterns = [
    path('catalogue/', BookCatalogue.as_view(),name='book catalogue' ),
    path('add-book/',AddBook.as_view(),name='add book'),
    path('book-details/<int:pk>/',BookDetails.as_view(),name='book details'),


]


