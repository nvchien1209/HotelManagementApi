from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from .models import Hotel, Room, RoomType
from .serializers import HotelSerializer, RoomSerializer, RoomTypeSerializer, HotelDetailSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Stars', 'Name']  # Lọc theo số sao và tên khách sạn

    def list(self, request, *args, **kwargs):
        """
        Lấy danh sách khách sạn với thông báo.
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": f"Có tổng cộng {len(serializer.data)} khách sạn được tìm thấy!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return HotelDetailSerializer
        return HotelSerializer  
    def create(self, request, *args, **kwargs):
        """
        Xử lý tạo mới khách sạn với thông báo phản hồi chi tiết.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                "message": "Khách sạn đã được tạo thành công!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Tạo khách sạn không thành công.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Cập nhật thông tin khách sạn.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                "message": "Cập nhật thông tin khách sạn thành công!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Cập nhật khách sạn không thành công.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Xóa khách sạn với thông báo phản hồi.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": "Khách sạn đã được xóa thành công!"
        }, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        """
        Lấy thông tin chi tiết của khách sạn.
        """
        try:
            instance = self.get_object()  # Nếu không tìm thấy, sẽ tự động ném lỗi 404
            serializer = self.get_serializer(instance)
            return Response({
                "message": "Lấy thông tin khách sạn thành công!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        
        except Hotel.DoesNotExist:
            raise NotFound({"message": "Không tìm thấy khách sạn!"})

    
class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Capacity']  # Lọc theo sức chứa

    def get_object(self):
        """
        Xử lý lỗi khi loại phòng không tồn tại.
        """
        try:
            return super().get_object()
        except RoomType.DoesNotExist:
            raise NotFound({"message": "Không tìm thấy loại phòng!"})

    def list(self, request, *args, **kwargs):
        """
        Lấy danh sách các loại phòng.
        """
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({"message": "Không có loại phòng nào!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": f"Có tổng cộng {len(serializer.data)} loại phòng được tìm thấy!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Lấy thông tin chi tiết của một loại phòng.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "message": "Lấy thông tin loại phòng thành công!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Tạo mới một loại phòng.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                "message": "Tạo loại phòng thành công!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Tạo loại phòng thất bại!",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Cập nhật thông tin loại phòng.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                "message": "Cập nhật loại phòng thành công!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Cập nhật loại phòng thất bại!",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Xóa loại phòng.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": "Xóa loại phòng thành công!"
        }, status=status.HTTP_204_NO_CONTENT)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Hotel', 'Room_type', 'Status']  # Lọc theo khách sạn, loại phòng và trạng thái

    def get_object(self):
        """
        Xử lý lỗi khi phòng không tồn tại.
        """
        try:
            return super().get_object()
        except Room.DoesNotExist:
            raise NotFound({"message": "Không tìm thấy phòng!"})

    def list(self, request, *args, **kwargs):
        """
        Lấy danh sách các phòng.
        """
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({"message": "Không có phòng nào!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": f"Có tổng cộng {len(serializer.data)} phòng được tìm thấy!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Lấy thông tin chi tiết của một phòng.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            "message": "Lấy thông tin phòng thành công!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Tạo mới một phòng.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                "message": "Tạo phòng thành công!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Tạo phòng thất bại!",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Cập nhật thông tin phòng.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response({
                "message": "Cập nhật phòng thành công!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Cập nhật phòng thất bại!",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Xóa phòng.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": "Xóa phòng thành công!"
        }, status=status.HTTP_204_NO_CONTENT)
