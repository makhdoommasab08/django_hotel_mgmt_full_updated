
from django.urls import path
from . import views
app_name = 'bookings'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/<int:room_id>/', views.create_booking, name='create'),
    path('booking/<int:pk>/', views.detail, name='detail'),
]
