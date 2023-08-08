
from django.test import TestCase

from web_magazine.accounts.forms import LoginForm, CreateUserForm
from web_magazine.accounts.models import AppUser


class CreateUserFromTestCase(TestCase):
    def test_valid_form_data(self):
        form_data = {
            'email':'test@test.com',
            'password1':'testpassword',
            'password2':'testpassword',
        }
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_data(self):
        form_data = {
            'email':'test@test.com',
            'password1': 'testpassword1',
            'password2': 'testpassword2',
        }
        form = CreateUserForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_blank_form_data(self):
        form_data = {
            'email': '',
            'password1': '',
            'password2':'',
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_username_is_required(self):
        form_data = {
            'email':'',
            'password1':'testpassword',
            'password2':'testpassword',
        }
        form = CreateUserForm(data=form_data)
        self.assertFormError(form, 'email', 'This field is required.')

    def test_password_is_required(self):
        form_data = {
            'email':'test@test.com',
            'password1':'',
            'password2':'',
        }
        form = CreateUserForm(data=form_data)
        self.assertFormError(form,'password1','This field is required.')
        self.assertFormError(form,'password2','This field is required.')
