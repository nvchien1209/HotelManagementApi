# Generated by Django 4.2.20 on 2025-03-26 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='citizen_code',
            new_name='Citizen_code',
        ),
    ]
