# Generated by Django 3.1.1 on 2020-12-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0008_auto_20201220_0939'),
    ]

    operations = [
        migrations.DeleteModel(
            name='chek',
        ),
        migrations.AlterField(
            model_name='question',
            name='questID',
            field=models.CharField(default='c43f156112007403', max_length=16),
        ),
        migrations.AlterField(
            model_name='testpackage',
            name='testID',
            field=models.CharField(default='983eb3e8627e3a20', max_length=16),
        ),
        migrations.AlterField(
            model_name='testtaker',
            name='testTakerID',
            field=models.CharField(default='e0b4e25c3218f7df', max_length=16),
        ),
    ]
