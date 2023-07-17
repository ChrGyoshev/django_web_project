from django import forms

from web_magazine.cart.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'