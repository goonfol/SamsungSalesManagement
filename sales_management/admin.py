from django.contrib import admin
from . models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


admin.site.register(Product)
admin.site.register(ProductVariation)
admin.site.register(Region)
admin.site.register(Area)
admin.site.register(District)
admin.site.register(Territory)
admin.site.register(Outlet)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'gender', 'phone',
                  'join_date', 'date_of_birth',
                  'address', 'picture', 'is_active',)}
         ),
    )



admin.site.register(CustomUser, CustomUserAdmin)