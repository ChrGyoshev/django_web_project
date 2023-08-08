from django.core.exceptions import ValidationError
from django.test import TestCase

from web_magazine.book.models import Author, Book


class BookModelTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name='John',last_name='Smith')

    def test_book_creation(self):
        book_data = {
            'title':"Nice book",
            'description':'This book tests',
            'price': 19.90,
            'cover':'path/to/book/example.jpg',
            'author':self.author,
        }

        book= Book.objects.create(**book_data)

        self.assertEqual(book.title,'Nice book')
        self.assertEqual(book.description,'This book tests')
        self.assertEqual(book.price, 19.90)
        self.assertEqual(book.cover,'path/to/book/example.jpg')
        self.assertEqual(book.author,self.author)


class TestAuthorModelTestCase(TestCase):
    def setUp(self):

        self.author_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
        }
    def test_required_fields(self):
        with self.assertRaises(ValidationError) as ex:
            author = Author.objects.create(first_name='',last_name='')
            author.full_clean()
        expected_error_msg = 'This field cannot be blank.'
        self.assertEqual(ex.exception.message_dict['first_name'][0],expected_error_msg)
        self.assertEqual(ex.exception.message_dict['last_name'][0],expected_error_msg)

    def test_author_creation(self):

        author = Author.objects.create(**self.author_data)
        self.assertEqual(author.first_name,'Jane')
        self.assertEqual(author.last_name,'Smith')

    def test_author_save(self):
        author = Author(**self.author_data)
        author.save()

        author_from_db = Author.objects.get(pk=author.pk)
        self.assertEqual(author,author_from_db)
