from django.contrib import admin

from web_magazine.cart.models import  Order


# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ['profile', 'quantity', 'created', 'status', 'price']
    readonly_fields = ['book', 'quantity', 'profile', ]
    exclude = ['created',]
    list_filter = ['created',]
    ordering = ['created',]

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        readonly_fields = self.get_readonly_fields(request, obj)
        return readonly_fields + [field for field in fields if field not in readonly_fields]

    def save_model(self, request, obj, form, change):
        if obj.status == 'Finished':
            obj.delete()
        else:
            super().save_model(request, obj, form, change)





