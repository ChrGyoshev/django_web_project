from django.contrib import admin

from web_magazine.cart.models import Cart


# Register your models here.

@admin.register(Cart)
class BookAdmin(admin.ModelAdmin):
    pass