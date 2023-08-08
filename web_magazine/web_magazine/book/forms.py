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
        label='Author First Name',
        widget=forms.TextInput(attrs={'placeholder': 'Author First Name'}),

    )
    author_last_name = forms.CharField(
        max_length=30,
        required=False,
        label='Author Last Name',
    widget = forms.TextInput(attrs={'placeholder': 'Author Last Name'}),
    )

    cover = forms.ImageField(
        error_messages={
            'required': 'Please upload an image for the book cover.'
        }
    )


    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'cover', 'author', 'author_first_name', 'author_last_name']

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Book Title'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'




class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=50,
    )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['search'].widget.attrs['placeholder'] = "Search for your favourite book or author"






