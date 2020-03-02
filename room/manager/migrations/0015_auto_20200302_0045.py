# Generated by Django 3.0.3 on 2020-03-01 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_auto_20200302_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_booking',
            name='booking_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='old_booking',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.new_booking'),
        ),
    ]
