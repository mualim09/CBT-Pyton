# Generated by Django 3.1.1 on 2021-07-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0020_auto_20210728_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testpackage',
            name='passwordTest',
            field=models.CharField(blank=True, default=None, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='testpackage',
            name='welcomeMessage',
            field=models.TextField(blank=True, null=True),
        ),
    ]