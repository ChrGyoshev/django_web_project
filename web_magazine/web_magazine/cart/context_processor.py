

from django.http import request

from web_magazine.cart.models import Cart


def CartItemsPerProfile(request):
    books_cart_count = 0
    if request.user.is_authenticated:
        profile = request.user.profile
        profile_books = Cart.objects.filter(profile=profile)

        for cart_item in profile_books:
            quantity = cart_item.quantity
            books_cart_count += quantity
    else:
        books_cart_count = None

    return {
        'profile_books': books_cart_count,
    }
