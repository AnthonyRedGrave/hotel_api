from django.shortcuts import render
from rest_framework.response import Response

from .models import Hotel, Room, Book
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import HotelSerializer, RoomSerializer
from rest_framework.decorators import action
from datetime import datetime


# Просмотр отелей и номеров
# Поиск отелей
# Бронирование номеров


class HotelViewSet(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated, ]


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, ]

    def list(self, request, *args, **kwargs):
        for book in Book.objects.all():
            if datetime.now().timestamp() > book.date_finish.timestamp():
                book.room.is_booked = False
                book.room.save()
                book.delete()

        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=['POST'])
    def book(self, request, pk=None):
        room = self.get_object()
        date_finish = request.POST['date_finish']
        date_finish = datetime.strptime(date_finish, "%d/%m/%Y %H:%M")

        Book.objects.create(
            owner = request.user,
            room = room,
            date_finish = date_finish
        )
        return Response(data={"Бронь": "Успешно забронирована!"})
