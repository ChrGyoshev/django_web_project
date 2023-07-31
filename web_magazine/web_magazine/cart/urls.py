from django.urls import path
from web_magazine.cart.views import CartViewAdd, CartViewUser, DeleteItemFromCart, BuyNow, ShipmentProcess, Finish, \
    SuccessOrder

urlpatterns = [
    path('<int:pk>/', CartViewAdd.as_view(), name='cart add'),
    path('check-out/', CartViewUser.as_view(), name='cart view'),
    path('delete/<int:pk>/',DeleteItemFromCart.as_view(),name='delete item from cart'),
    path('buy-now/', BuyNow.as_view(),name='buy now'),
    path('process/', ShipmentProcess.as_view(), name='process shippment'),
    path('finish-order/<int:pk>', Finish,name='finish order'),
    path('success-order/', SuccessOrder.as_view(),name='success order'),


]