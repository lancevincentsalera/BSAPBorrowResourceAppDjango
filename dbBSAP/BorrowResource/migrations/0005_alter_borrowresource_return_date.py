# Generated by Django 4.2.6 on 2023-11-16 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BorrowResource', '0004_alter_borrowresource_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowresource',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 23, 3, 29, 39, 523525, tzinfo=datetime.timezone.utc)),
        ),
    ]
