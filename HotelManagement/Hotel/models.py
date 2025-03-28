from django.db import models

class Hotel(models.Model):
    HotelId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=15)
    Email = models.CharField(max_length=255)
    Stars = models.IntegerField()
    Checkin_time = models.TimeField()
    Checkout_time = models.TimeField()

    def __str__(self):
        return self.Name

class RoomType(models.Model):
    RoomTypeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=255)
    Price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    Capacity = models.IntegerField()

    def __str__(self):
        return self.Name

class Room(models.Model):
    RoomId = models.AutoField(primary_key=True)
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    Room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='rooms')
    Status = models.CharField(max_length=20)  

    def __str__(self):
        return f"Room {self.RoomId} at {self.Hotel.Name}"