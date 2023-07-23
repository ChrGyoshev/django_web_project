from django.db import transaction
from django.db.models import Sum, F
from django.shortcuts import redirect, get_object_or_404, render
from django.utils import timezone
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
        context = super().get_context_data(*args, **kwargs)
        queryset = self.get_queryset()
        queryset = queryset.annotate(total_price=F('book__price') * F('quantity'))
        total_amount_of_books = sum(item.total_price for item in queryset)
        context['total_amount'] = total_amount_of_books
        context['books'] = queryset
        return context


class DeleteItemFromCart(views.View):

    def get(self, request, pk):
        cart_books = Cart.objects.filter(profile=self.request.user.profile)
        book = get_object_or_404(cart_books, pk=pk)
        if book.quantity == 1:
            book.delete()
        else:
            book.quantity -= 1
            book.save()
        return redirect('cart view')


class BuyNow(views.View):
    template_name = 'buy-now.html'  # Replace this with your template name


    def post(self, request, *args, **kwargs):
        # Assuming you have a logged-in user with a profile
        profile = request.user.profile

        # Fetch items from the cart
        cart_items = Cart.objects.filter(profile=profile)



        with transaction.atomic():
            for cart_item in cart_items:
                created_time = timezone.now() +timezone.timedelta(hours=3)
                Order.objects.create(
                    profile=profile,
                    book=cart_item.book,
                    quantity=cart_item.quantity,
                    created= created_time,





                )
                cart_item.delete()




        return redirect('process shippment')



class ShipmentProcess(views.ListView):
    template_name = 'shipment-process.html'
    model = Order

    def get(self, request, *args, **kwargs):
        profiles = Profile.objects.all()

        # You can get the related orders for each profile in the loop below

        for profile in profiles:
            profile.orders = Order.objects.filter(profile=profile)

        context = {
            'profiles': profiles,
        }

        return render(request, self.template_name, context)







def Finish(request, pk):

    profile = Profile.objects.get(pk=pk)

    if request.method == 'POST':

        form = OrderCreateForm(request.POST,)

        if form.is_valid():

            new_status = form.cleaned_data['status']


            Order.objects.filter(profile=profile).update(status=new_status)
            return redirect('process shippment')



    else:
        # Create an empty form for GET request
        form = OrderCreateForm(instance=Order.objects.filter(profile=profile).first())

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'finish-order.html', context)

