# Generated by Django 4.1.2 on 2022-12-05 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_alter_orderaddfield_order_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderaddfield',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 5, 9, 34, 4, 831724)),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2022, 12, 5, 9, 34, 4, 831724)),
        ),
    ]
