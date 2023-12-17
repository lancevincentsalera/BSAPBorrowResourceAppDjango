# Generated by Django 4.2.6 on 2023-10-10 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BorrowResource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('user_type', models.CharField(choices=[('R', 'Resident'), ('O', 'Organization'), ('A', 'Admin')], max_length=1)),
                ('admin_status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('user_type', models.CharField(choices=[('R', 'Resident'), ('O', 'Organization'), ('A', 'Admin')], max_length=1)),
                ('organization_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('user_type', models.CharField(choices=[('R', 'Resident'), ('O', 'Organization'), ('A', 'Admin')], max_length=1)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('birth_date', models.DateField()),
                ('present_address', models.CharField(max_length=50)),
                ('borrowed_resources', models.ManyToManyField(through='BorrowResource.BorrowResource', to='BorrowResource.resource')),
            ],
            options={
                'db_table': 'Resident',
            },
        ),
    ]