from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/customer/', include('customer.urls')),  # API khách hàng: /api/customer/
    path('api/hotel/', include('Hotel.urls')),     # API khách sạn: /api/hotel/
    path('api/booking/', include('booking.urls')),  #API booking: /api/booking
]