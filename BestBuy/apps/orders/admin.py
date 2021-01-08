import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from django.http import request


from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'paid', 'country', 'postal_code', 'city', 'street' , 'building', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta