from rest_framework import serializers
from .models import Booking, Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['PaymentID', 'Booking', 'Amount', 'PaymentDate', 'PaymentMethod']

class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['PaymentID', 'Amount', 'PaymentDate', 'PaymentMethod']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['BookingID', 'Customer', 'RoomNumber', 'CheckinDate', 'CheckoutDate', 'TotalPrice']

class BookingDetailSerializer(serializers.ModelSerializer):
    payments = PaymentDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Booking
        fields = ['BookingID', 'Customer', 'RoomNumber', 'CheckinDate', 'CheckoutDate', 'TotalPrice', 'payments']