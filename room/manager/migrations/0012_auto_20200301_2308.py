# Generated by Django 3.0.3 on 2020-03-01 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_new_booking_added_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_booking',
            old_name='added_by',
            new_name='customer',
        ),
    ]