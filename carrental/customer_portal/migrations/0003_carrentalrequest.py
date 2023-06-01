# Generated by Django 4.0.6 on 2023-05-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0002_remove_user_aadharcard_remove_user_drivinglicense_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarRentalRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up_location', models.CharField(max_length=100)),
                ('pick_up_date', models.DateField()),
                ('drop_off_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('drop_off_time', models.TimeField()),
            ],
        ),
    ]
