# Generated by Django 3.1.1 on 2021-06-10 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_auto_20210610_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtaker',
            name='timeFinish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 10, 29, 18, 355662), null=True),
        ),
        migrations.AlterField(
            model_name='testtaker',
            name='timeStart',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 10, 29, 18, 355634), null=True),
        ),
    ]
