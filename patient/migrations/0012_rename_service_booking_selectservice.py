# Generated by Django 3.2.9 on 2022-03-20 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_rename_select_service_booking_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='service',
            new_name='selectservice',
        ),
    ]
