# Generated by Django 3.0.3 on 2020-03-01 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_auto_20200302_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='old_booking',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
