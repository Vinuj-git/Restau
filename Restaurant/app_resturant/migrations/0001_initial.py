# Generated by Django 3.2 on 2022-05-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurantmodule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=55)),
                ('city', models.CharField(max_length=55)),
                ('pincode', models.IntegerField()),
                ('total_like', models.IntegerField()),
                ('total_save', models.IntegerField()),
            ],
        ),
    ]
