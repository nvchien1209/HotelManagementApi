from django.db import models
from customer.models import Customer
from Hotel.models import Room

class Booking(models.Model):
    BookingID = models.AutoField(primary_key=True)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    RoomNumber = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    CheckinDate = models.DateField()
    CheckoutDate = models.DateField()
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)
      
    def __str__(self):
        return f"Booking {self.BookingID} - {self.Customer.get_full_name()}"

class Payment(models.Model):
    Payment_Methods = (
        ('Cash', 'Tiền mặt'),
        ('Card', 'Quẹt thẻ'),
        ('Banking', 'Chuyển khoản')
    )
    PaymentID = models.AutoField(primary_key=True)
    Booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='payments')
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentDate = models.DateField()
    PaymentMethod = models.CharField(max_length=50, choices=Payment_Methods)

    def __str__(self):
        return f"Payment {self.PaymentID} for Booking {self.Booking.BookingID}"
