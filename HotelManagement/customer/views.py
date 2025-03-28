from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint cho phép thực hiện các thao tác CRUD trên Customer
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {"message": "Tạo khách hàng thành công!", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Tạo khách hàng không thành công!", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                {"message": "Cập nhật khách hàng thành công!", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Cập nhật khách hàng thất bại!", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
            return Response(
                {"message": "Xóa khách hàng thành công!"}, 
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            return Response(
                {"message": "Xóa khách hàng không thành công!", "error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=False, methods=['get'], url_path='search')
    def search_customers(self, request):
        """
        API để tìm kiếm khách hàng theo tên hoặc số điện thoại
        """
        query = request.query_params.get('q', '')
        if not query:
            return Response(
                {"message": "Vui lòng nhập từ khóa tìm kiếm."}, 
                status=status.HTTP_400_BAD_REQUEST,
            )

        customers = Customer.objects.filter(
            FirstName__icontains=query
        ) | Customer.objects.filter(
            LastName__icontains=query
        ) | Customer.objects.filter(
            Phone__icontains=query
        )

        if customers.exists():
            serializer = self.get_serializer(customers, many=True)
            return Response(
                {"message": "Tìm kiếm thành công!", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"message": "Không tìm thấy khách hàng nào phù hợp."}, 
            status=status.HTTP_404_NOT_FOUND,
        )
