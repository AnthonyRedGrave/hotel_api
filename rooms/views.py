from django.shortcuts import render
from .models import Hotel, Room, Book
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import HotelSerializer

# Просмотр отелей и номеров
# Поиск отелей
# Бронирование номеров


class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated, ]

