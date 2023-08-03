from django.contrib import admin

from web_magazine.cart.models import  Order


# Register your models here.

@admin.register(Order)
class BookAdmin(admin.ModelAdmin):

    list_display = ['profile', 'quantity', 'created', 'status', 'price']
    readonly_fields = ['quantity', 'book', 'profile', ]
    exclude = ['created',]

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        readonly_fields = self.get_readonly_fields(request, obj)
        return readonly_fields + [field for field in fields if field not in readonly_fields]

    # Customize the column header in the admin interface



