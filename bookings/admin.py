
from django.contrib import admin
from .models import Guest, Booking, Payment

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','phone')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','guest','room','check_in','check_out','status','total_amount')
    list_filter = ('status',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking','amount','paid_at','provider')
