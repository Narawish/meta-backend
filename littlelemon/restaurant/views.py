from django.shortcuts import render
from .models import Menu, Booking
from django.contrib.auth.models import User
from .serializers import MenuSerializers, BookingSerializers, UserSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import RetrieveUpdateAPIView, DestroyAPIView, ListCreateAPIView
# Create your views here.
def index(request):
    return render(request, 'index.html', {})
 
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    permission_classes = [IsAuthenticated]

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [IsAuthenticated]

class SingleBookingView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [IsAuthenticated]

