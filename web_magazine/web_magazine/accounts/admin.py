
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


from web_magazine.accounts.models import AppUser, Profile


@admin.register(AppUser)
class UserAdmin(UserAdmin):
    filter_horizontal = ('groups', 'user_permissions',)
    list_display = ('email','is_staff',)



    fieldsets = (
        (None, {"fields": ("email", "password")}),

        (
            ("Permissions"),
            {
                "fields": (

                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),

    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


    list_filter = ("is_staff", "is_superuser",  "groups")
    search_fields = ("email",  "email")
    ordering = ("email",)





