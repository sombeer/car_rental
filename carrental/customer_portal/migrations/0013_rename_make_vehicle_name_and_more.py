# Generated by Django 4.0.6 on 2023-06-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0012_customer_remove_rentalbooking_pickup_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='make',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='rental_price',
            new_name='rentPerHour',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='color',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_type',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='model',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='year',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='fuelType',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.CharField(default='none', max_length=1000),
        ),
    ]