from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label='Select an existing author',
        required=False
    )
    author_first_name = forms.CharField(
        max_length=30,
        required=False,
        label='Author First Name'
    )
    author_last_name = forms.CharField(
        max_length=30,
        required=False,
        label='Author Last Name'
    )

    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'cover', 'author', 'author_first_name', 'author_last_name']








