# Generated by Django 3.0.3 on 2020-03-01 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20200301_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_booking',
            old_name='add',
            new_name='new',
        ),
    ]
