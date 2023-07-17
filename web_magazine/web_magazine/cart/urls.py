from django.urls import path
from web_magazine.cart.views import CartViewAdd, CartViewUser, DeleteItemFromCart, BuyNow, Finished

urlpatterns = [
    path('<int:pk>/', CartViewAdd.as_view(), name='cart add'),

    path('check-out/', CartViewUser.as_view(), name='cart view'),
    path('delete/<int:pk>/',DeleteItemFromCart.as_view(),name='delete item from cart'),
    path('buy-now/', BuyNow.as_view(),name='buy now'),

    path('finished/',Finished.as_view(),name='finished'),
]