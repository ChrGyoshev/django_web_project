

from django.http import request

from web_magazine.cart.models import Order


def CartItemsPerProfile(request):
    profile =request.user.profile
    profile_books = Order.objects.filter(profile=profile).count()
    return {
        'profile_books':profile_books,
    }
