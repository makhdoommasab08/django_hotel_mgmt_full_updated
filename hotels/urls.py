
from django.urls import path
from . import views
app_name = 'hotels'
urlpatterns = [
    path('', views.index, name='index'),
    path('hotel/<int:pk>/', views.hotel_detail, name='detail'),
]
