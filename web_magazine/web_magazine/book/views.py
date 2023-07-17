from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic as view
from web_magazine.book.forms import BookForm
from web_magazine.book.models import Book, Author


class BookCatalogue(view.ListView):
    template_name = 'catalogue.html'
    model = Book
    paginate_by = 6


class AddBook(UserPassesTestMixin, view.CreateView):
    template_name = 'add-book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.groups.filter(name='EditBook').exists() or self.request.user.is_superuser

    def form_valid(self, form):
        author = form.cleaned_data['author']
        author_first_name = form.cleaned_data['author_first_name']
        author_last_name = form.cleaned_data['author_last_name']

        if not author and not (author_first_name and author_last_name):
            form.add_error(
                None, 'Please select an existing author or enter both first and last names for a new author.'
            )
            return self.form_invalid(form)

        if not author:
            author_exists = Author.objects.filter(
                first_name=author_first_name, last_name=author_last_name
            ).exists()
            if author_exists:
                form.add_error(
                    None, 'An author with the given first name and last name already exists.'
                )
                return self.form_invalid(form)

            author = Author.objects.create(first_name=author_first_name, last_name=author_last_name)

        book = form.save(commit=False)
        book.author = author
        book.save()

        return super().form_valid(form)



