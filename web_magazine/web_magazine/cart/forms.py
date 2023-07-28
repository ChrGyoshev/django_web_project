from django import forms
from django.core.validators import RegexValidator
from web_magazine.cart.models import Order


phone_regex_validator = RegexValidator(
    regex=r'^\+\d{1,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'status',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].initial= '---'


class PhoneOrderForm(forms.ModelForm):
    phone = forms.CharField(validators=[phone_regex_validator], max_length=17, required=True)

    class Meta:
        model = Order
        fields = ['phone','address',]
