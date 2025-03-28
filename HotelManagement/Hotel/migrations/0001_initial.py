# Generated by Django 4.2.20 on 2025-03-27 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('HotelId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=255)),
                ('Stars', models.IntegerField()),
                ('Checkin_time', models.TimeField()),
                ('Checkout_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('RoomTypeID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=255)),
                ('Price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('RoomId', models.AutoField(primary_key=True, serialize=False)),
                ('Status', models.CharField(max_length=20)),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='Hotel.hotel')),
                ('Room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='Hotel.roomtype')),
            ],
        ),
    ]
