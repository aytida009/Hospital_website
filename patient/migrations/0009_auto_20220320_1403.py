# Generated by Django 3.2.9 on 2022-03-20 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_auto_20220320_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='selectservice',
            new_name='select_service',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='specialrequest',
            new_name='special_request',
        ),
    ]