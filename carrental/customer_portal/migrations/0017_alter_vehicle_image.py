# Generated by Django 4.0.6 on 2023-06-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0016_alter_customer_options_alter_customer_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(upload_to='car_images'),
        ),
    ]
