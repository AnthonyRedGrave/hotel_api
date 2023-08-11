from rest_framework import serializers
from .models import Hotel, Room


class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.SerializerMethodField()

    def get_hotel(self, room):
        return room.hotel.title

    class Meta:
        model = Room
        fields = ['id', 'number', 'count_places', 'price', 'is_booked', 'hotel']

class RoomHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'number', 'count_places', 'price', 'is_booked']


class HotelSerializer(serializers.ModelSerializer):
    rooms = serializers.SerializerMethodField()

    def get_rooms(self, hotel):
        serializer= RoomHotelSerializer(hotel.rooms.all(), many=True)

        return serializer.data


    class Meta:
        model = Hotel
        fields = ['id', 'title', 'description', 'rooms']