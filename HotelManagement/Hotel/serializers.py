from rest_framework import serializers
from .models import Hotel, Room, RoomType

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['RoomTypeID', 'Name', 'Description', 'Price_per_night', 'Capacity']

class RoomSerializer(serializers.ModelSerializer):
    room_type_detail = RoomTypeSerializer(source='Room_type', read_only=True)
    
    class Meta:
        model = Room
        fields = ['RoomId', 'Hotel', 'Room_type', 'room_type_detail', 'Status']

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['HotelId', 'Name', 'Stars', ]

class HotelDetailSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    
    class Meta:
        model = Hotel
        fields = ['HotelId', 'Name', 'Address', 'Phone', 'Email', 'Stars', 
                 'Checkin_time', 'Checkout_time', 'rooms']