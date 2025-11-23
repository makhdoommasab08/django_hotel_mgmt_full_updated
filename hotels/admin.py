
from django.contrib import admin
from .models import Hotel, RoomType, Room, Amenity

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','city','country','phone')
    search_fields = ('name','city','country')

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name','hotel','capacity','base_price')
    list_filter = ('hotel',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number','room_type','floor','is_active')
    list_filter = ('room_type__hotel','is_active')

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)
