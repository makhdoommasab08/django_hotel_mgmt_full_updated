
from django.shortcuts import render, get_object_or_404, redirect
from .models import Booking, Guest
from hotels.models import Hotel, RoomType, Room
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bookings = Booking.objects.all().order_by('-created_at')[:50]
    return render(request, 'bookings/index.html', {'bookings': bookings})

def create_booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        # Simplified demo: create guest + booking with posted data
        guest = Guest.objects.create(
            first_name=request.POST.get('first_name','Guest'),
            last_name=request.POST.get('last_name',''),
            email=request.POST.get('email','guest@example.com'),
            phone=request.POST.get('phone','')
        )
        booking = Booking.objects.create(
            room=room,
            guest=guest,
            check_in=request.POST.get('check_in'),
            check_out=request.POST.get('check_out'),
            total_amount=request.POST.get('total_amount', 0),
            status='confirmed'
        )
        return redirect(reverse('bookings:detail', args=[booking.id]))
    return render(request, 'bookings/create.html', {'room': room})

def detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'bookings/detail.html', {'booking': booking})
