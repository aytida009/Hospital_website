# Generated by Django 3.2.9 on 2022-03-19 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_auto_20220319_0330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='AppointmentDate',
            new_name='appointmentdate',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='AppointmentTime',
            new_name='appointmenttime',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='FullName',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='SelectService',
            new_name='selectservice',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='SpecialRequest',
            new_name='specialrequest',
        ),
    ]