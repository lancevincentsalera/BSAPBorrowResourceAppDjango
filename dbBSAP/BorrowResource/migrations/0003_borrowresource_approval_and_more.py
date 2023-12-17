# Generated by Django 4.2.6 on 2023-11-02 09:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CreateAccount', '0003_alter_admin_username_alter_organization_username_and_more'),
        ('BorrowResource', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowresource',
            name='approval',
            field=models.CharField(choices=[('A', 'Approve'), ('P', 'Pending'), ('R', 'Reject')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='borrowresource',
            name='borrow_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='borrowresource',
            name='org_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CreateAccount.organization'),
        ),
        migrations.AlterField(
            model_name='borrowresource',
            name='resident_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CreateAccount.resident'),
        ),
        migrations.AlterField(
            model_name='borrowresource',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 9, 9, 47, 44, 707828, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='resource',
            name='resource_name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]