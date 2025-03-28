from django.db import models

class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    DateOfBirth = models.DateField()
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=15)
    Citizen_code = models.CharField(max_length=20, unique=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['LastName', 'FirstName']
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
    
    def get_full_name(self):
        return f"{self.FirstName} {self.LastName}"
    
    def get_short_name(self):
        return self.FirstName