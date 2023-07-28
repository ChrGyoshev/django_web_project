from django import forms
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.db import transaction, models
from django.db.models import Sum, F

from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic as views

from web_magazine.accounts.models import Profile
from web_magazine.book.models import Book
from web_magazine.cart.forms import OrderCreateForm, PhoneOrderForm

from web_magazine.cart.models import Cart, Order


class CartViewAdd(LoginRequiredMixin,views.TemplateView):
    model = Book
    template_name = 'cart.html'
    context_object_name = 'books'

    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to access this page.")
        return redirect(reverse_lazy('index'))

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
        context['form'] = PhoneOrderForm()
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

    def get_cart_items(self):
        # Fetch items from the cart
        profile = self.request.user.profile
        return Cart.objects.filter(profile=profile)

    def post(self, request, *args, **kwargs):
        form = PhoneOrderForm(request.POST)
        cart_items = self.get_cart_items()

        if form.is_valid():
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']

            self.request.user.profile.save()

            with transaction.atomic():
                for cart_item in cart_items:
                    created_time = timezone.now() + timezone.timedelta(hours=3)
                    Order.objects.create(
                        profile=self.request.user.profile,
                        book=cart_item.book,
                        quantity=cart_item.quantity,
                        created=created_time,
                        price=cart_item.book.price,
                        phone=phone,
                        address=address,
                    )
                    cart_item.delete()
                Order.objects.filter(profile=self.request.user.profile).update(status='Pending')

            return redirect('success order')

        context = {
            'form': form,
            'books': cart_items,
        }
        return render(request, "cart-check-out.html", context)


class ShipmentProcess(LoginRequiredMixin, UserPassesTestMixin, views.ListView):
    template_name = 'shipment-process.html'
    model = Order


    def test_func(self):
        return self.request.user.groups.filter(name='EditBook').exists() or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to access this page.")
        return redirect(reverse_lazy('cart view'))

    def get(self, request, *args, **kwargs):


        profiles = Profile.objects.all()

        for profile in profiles:
            profile.orders = Order.objects.filter(profile=profile)
            total_price = profile.orders.aggregate(total_price=Sum(models.F('price') * models.F('quantity')))[
                'total_price']
            profile.total_price = total_price if total_price is not None else 0

        for profile in profiles:
            profile.orders = Order.objects.filter(profile=profile)

        form = OrderCreateForm()
        context = {
            'profiles': profiles,
            'form':form,

        }

        return render(request, self.template_name, context)








def Finish(request, pk):
    profile = Profile.objects.get(pk=pk)
    book = Order.objects.filter(profile=profile)



    if request.method == 'POST':

        form = OrderCreateForm(request.POST,instance=book.last())
        if form.is_valid():
            new_status = form.cleaned_data['status']
            if new_status == 'Finished':
                book.delete()
            else:
                book.update(status=form.cleaned_data['status'])
                form.save()

            return redirect('process shippment')
    else:
        form = OrderCreateForm()

    context = {
        'form': form,
    }
    return render(request, 'shipment-process.html', context)




class SuccessOrder(views.TemplateView):
    template_name = 'order-succsess.html'