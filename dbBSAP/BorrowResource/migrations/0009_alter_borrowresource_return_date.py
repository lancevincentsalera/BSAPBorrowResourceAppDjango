# Generated by Django 4.2.6 on 2023-11-16 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BorrowResource', '0008_alter_borrowresource_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowresource',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 23, 14, 3, 45, 210204, tzinfo=datetime.timezone.utc)),
        ),
    ]