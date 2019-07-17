from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import UserAdminChangeForm, UserAdminCreationForm
# Register your models here.


class MyUserAdmin(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('admin', 'staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2')}
         ),
    )
    list_display = ('email', 'first_name', 'admin')
    list_filter = ('admin',)
    filter_horizontal = ()
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    ordering = ('email', 'first_name', 'last_name')


admin.site.register(User, MyUserAdmin)
