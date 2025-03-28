from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def get_full_name(self, obj):
        return f"{obj.FirstName} {obj.LastName}"
    
    def get_age(self, obj):
        # Tính tuổi
        from datetime import date
        today = date.today()
        born = obj.DateOfBirth
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age
    
    def validate_Citizen_code(self, value):
        # Kiểm tra nếu citizen_code đã tồn tại khi tạo mới
        request = self.context.get('request')
        if request and request.method == 'POST':
            if Customer.objects.filter(Citizen_code=value).exists():
                raise serializers.ValidationError("Citizen code này đã tồn tại.")
        return value
    
    def validate_Phone(self, value):
        if not value:
            raise serializers.ValidationError("Số điện thoại không được để trống.")

        if not value.isdigit():
            raise serializers.ValidationError("Số điện thoại chỉ được chứa các chữ số.")
        
        if len(value) < 9 or len(value) > 15:
            raise serializers.ValidationError("Số điện thoại phải có từ 9 đến 15 chữ số.")

        return value
