from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
import ssl

from web_magazine.accounts.models import AppUser, Profile

ssl._create_default_https_context = ssl._create_unverified_context


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email','password1','password2',)
        field_classes = {"username": UsernameField}



class ChangeForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ('user',)
        widgets = {
            'phone':forms.TextInput(attrs={'value': '+359'})
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label=("Username"))
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        attrs={'data-theme':'dark'}
    ),error_messages={'required': 'You must pass the reCAPTCHA test'}
)
    remember_me = forms.BooleanField(label="remember Me",required=False)

