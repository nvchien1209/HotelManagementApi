from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Booking, Payment
from .serializers import BookingSerializer, BookingDetailSerializer, PaymentSerializer, PaymentDetailSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()

    def get_serializer_class(self):
        """Sử dụng BookingDetailSerializer khi lấy chi tiết một booking"""
        if self.action == 'retrieve':
            return BookingDetailSerializer
        return BookingSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "Đặt phòng thành công!", "data": response.data}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({"message": "Cập nhật thông tin đặt phòng thành công!", "data": response.data}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Xóa đặt phòng thành công!"}, status=status.HTTP_204_NO_CONTENT)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()

    def get_serializer_class(self):
        """Sử dụng PaymentDetailSerializer khi lấy chi tiết một payment"""
        if self.action == 'retrieve':
            return PaymentDetailSerializer
        return PaymentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "Thanh toán thành công!", "data": response.data}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({"message": "Cập nhật thông tin thanh toán thành công!", "data": response.data}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Xóa thanh toán thành công!"}, status=status.HTTP_204_NO_CONTENT)
