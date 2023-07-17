

from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Sum, F
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from web_magazine.accounts.models import Profile
from web_magazine.book.models import Book
from web_magazine.cart.forms import OrderCreateForm
from web_magazine.cart.models import Cart, Order


class CartViewAdd(views.TemplateView):
    model = Book
    template_name = 'cart.html'
    context_object_name = 'books'

    def get(self, request, *args, **kwargs):
        user = self.request.user.profile
        book = Book.objects.get(pk=self.kwargs['pk'])

        cart, created = Cart.objects.get_or_create(profile=user, book=book)
        if not created:
            cart.quantity += 1
            cart.save()
        return redirect('cart view')





class CartViewUser(views.ListView):
    model = Cart
    template_name = 'cart-check-out.html'

    def get_queryset(self):
        return Cart.objects.filter(profile=self.request.user.profile)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        queryset = self.get_queryset()
        queryset = queryset.annotate(total_price=F('book__price') * F('quantity'))
        total_amount_of_books = sum(item.total_price for item in queryset)
        context['total_amount'] = total_amount_of_books
        context['books'] = queryset
        return context




class DeleteItemFromCart(views.View):

    def get(self,request,pk):
        cart_books= Cart.objects.filter(profile=self.request.user.profile)
        book = get_object_or_404(cart_books, pk=pk)
        if book.quantity == 1:
            book.delete()
        else:
            book.quantity -=1
            book.save()
        return redirect('cart view')

   
class BuyNow(views.View):
    template_name = 'buy-now.html'  # Replace this with your template name

    def post(self, request, *args, **kwargs):
        # Assuming you have a logged-in user with a profile
        profile = request.user.profile

        # Fetch items from the cart
        cart_items = Cart.objects.filter(profile=profile)

        test= request.POST.get('adress')



        with transaction.atomic():
            for cart_item in cart_items:
                Order.objects.create(
                    profile=profile,
                    book=cart_item.book,
                    quantity=cart_item.quantity,


                )
                cart_item.delete()


        return redirect('finished')

class Finished(views.ListView):
    template_name = 'test.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self,*args,**kwargs):
        profile =self.request.user.profile

        queryset = Order.objects.filter(profile=profile)
        return queryset





