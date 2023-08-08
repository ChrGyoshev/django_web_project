

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from web_magazine.book.forms import SearchForm
from web_magazine.book.models import Author, validate_max_size


# Create your tests here.
class AuthorModelTest(TestCase):
    def setUp(self):
        self.author= Author.objects.create(first_name='John',last_name='Snow')

    def test_author_unique_together_constraint(self):

        with self.assertRaises(Exception):
            Author.objects.create(first_name='John', last_name="Snow")

class SearchFormTest(TestCase):
    def test_search_form_valid(self):
        form_data = {'search':'test query'}
        form =SearchForm(data=form_data)

    def test_search_form_empty(self):
        form_data = {}

        form = SearchForm(data=form_data)


        self.assertIn('search',form.errors)
        self.assertEqual(form.errors['search'],['This field is required.'])

    def test_form_max_length(self):
        form_data = {'search':'a'*51}
        form = SearchForm(data=form_data)
        self.assertIn('search',form.errors)
        self.assertEqual(form.errors['search'],['Ensure this value has at most 50 characters (it has 51).'])




class BookFormTestCase(TestCase):
    def test_book_cover_max_size(self):
        max_size = 6 * 1024 * 1024

        large_content = b'test_string' * (max_size + 1)
        large_cover = SimpleUploadedFile(
            name='large_cover.png',
            content=large_content,
            content_type='image/png'
            )
        with self.assertRaises(ValidationError) as context:
            validate_max_size(large_cover)
        self.assertEqual(
            context.exception.messages[0],
            "The book size must not exceed 5MB"
        )