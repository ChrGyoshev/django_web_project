

from django.http import request

from web_magazine.cart.models import Order


def CartItemsPerProfile(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        profile_books = Order.objects.filter(profile=profile).count()
    else:
        profile_books = None

    return {
        'profile_books': profile_books,
    }
