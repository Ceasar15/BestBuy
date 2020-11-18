from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model  =  CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'first_name', 'last_name', 'phone', 'last_login')
    list_filter = ('email', 'is_staff', 'is_active')
    verbose_name_plural = 'userprofile'
    fieldsets = (
        (None, {'fields': ('email', 'password', 'phone','first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
