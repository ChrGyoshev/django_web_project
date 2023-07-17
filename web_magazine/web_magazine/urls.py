from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from web_magazine.accounts.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index.as_view(),name='index'),

    path('account/', include('web_magazine.accounts.urls')),
    path('book/', include('web_magazine.book.urls')),
    path('cart/',include('web_magazine.cart.urls')),

    path("", include("allauth.urls")),  # most important
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
