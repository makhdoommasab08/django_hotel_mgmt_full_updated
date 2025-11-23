
from django.shortcuts import render, get_object_or_404
from .models import Hotel, RoomType

def index(request):
    hotels = Hotel.objects.all().order_by('name')
    return render(request, 'hotels/index.html', {'hotels': hotels})

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    room_types = hotel.room_types.all()
    return render(request, 'hotels/detail.html', {'hotel': hotel, 'room_types': room_types})
