# Generated by Django 4.2.6 on 2023-11-16 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BorrowResource', '0006_alter_borrowresource_approval_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowresource',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 23, 10, 45, 59, 99825, tzinfo=datetime.timezone.utc)),
        ),
    ]