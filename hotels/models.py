
from django.db import models
from django.urls import reverse

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='room_types')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    capacity = models.PositiveSmallIntegerField(default=2)
    base_price = models.DecimalField(max_digits=8, decimal_places=2)

    amenities = models.ManyToManyField(Amenity, blank=True, related_name='room_types')

    def __str__(self):
        return f"{self.hotel.name} - {self.name}"

class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT, related_name='rooms')
    number = models.CharField(max_length=20)
    floor = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room_type.hotel.name} - {self.number} ({self.room_type.name})"

    class Meta:
        unique_together = ('room_type', 'number')
