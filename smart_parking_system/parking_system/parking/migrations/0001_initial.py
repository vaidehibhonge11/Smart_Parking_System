# Generated by Django 5.0.2 on 2024-10-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=15)),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
