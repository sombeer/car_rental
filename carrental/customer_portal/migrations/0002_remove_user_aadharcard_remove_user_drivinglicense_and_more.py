# Generated by Django 4.2.1 on 2023-05-26 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='aadharCard',
        ),
        migrations.RemoveField(
            model_name='user',
            name='drivingLicense',
        ),
        migrations.AddField(
            model_name='user',
            name='aadharCardNo',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='drivingLicenseNo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobileNo',
            field=models.IntegerField(default=0),
        ),
    ]
