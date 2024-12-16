# app/admin.py
from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')
    search_fields = ('category_name',)

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_name',)
    search_fields = ('unit_name',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'stock_name', 'unit')
    list_filter = ('unit',)
    search_fields = ('stock_name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'mobile_no', 'group_type', 'category', 'follow_up_customer')
    list_filter = ('group_type', 'category', 'follow_up_customer')
    search_fields = ('customer_name', 'mobile_no')

@admin.register(AdvanceBooking)
class AdvanceBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'booking_date', 'due_date', 'need', 'total_load')
    list_filter = ('booking_date', 'due_date')
    search_fields = ('customer__customer_name', 'need')

@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'stock', 'total_load', 'unit')
    list_filter = ('stock', 'unit')
    search_fields = ('customer__customer_name', 'stock__stock_name')

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'stock', 'total_load', 'unit')
    list_filter = ('stock', 'unit')
    search_fields = ('customer__customer_name', 'stock__stock_name')