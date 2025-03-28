# Generated by Django 4.2.20 on 2025-03-28 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hotel', '0001_initial'),
        ('customer', '0002_rename_citizen_code_customer_citizen_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('BookingID', models.AutoField(primary_key=True, serialize=False)),
                ('CheckinDate', models.DateField()),
                ('CheckoutDate', models.DateField()),
                ('TotalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='customer.customer')),
                ('RoomNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='Hotel.room')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('PaymentID', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PaymentDate', models.DateField()),
                ('PaymentMethod', models.CharField(choices=[('Cash', 'Tiền mặt'), ('Card', 'Quẹt thẻ'), ('Banking', 'Chuyển khoản')], max_length=50)),
                ('Booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='booking.booking')),
            ],
        ),
    ]
