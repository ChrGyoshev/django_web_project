from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic as view
from web_magazine.book.forms import BookForm, SearchForm
from web_magazine.book.models import Book, Author
from web_magazine.custom_mixins import ModeratorAdminAccsses


class BookCatalogue(view.ListView):
    template_name = 'catalogue.html'
    model = Book
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        search = SearchForm(self.request.GET)
        if search.is_valid():
            search_query = search.cleaned_data.get('search', ' ')

            if search_query:
                queryset = queryset.filter(
                    Q(title__icontains=search_query) | Q(author__first_name__icontains=search_query) | Q(author__last_name__icontains=search_query))


        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)

        context['search'] = self.request.GET.get('search', '')
        context['form'] = SearchForm()
        return context



class AddBook(ModeratorAdminAccsses, view.CreateView):
    template_name = 'add-book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('index')



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



