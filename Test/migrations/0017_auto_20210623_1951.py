# Generated by Django 3.1.1 on 2021-06-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0016_auto_20210622_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testpackage',
            old_name='testScheduleFinish',
            new_name='testScheduleClose',
        ),
        migrations.AlterField(
            model_name='testpackage',
            name='settings',
            field=models.JSONField(blank=True, default={'canViewScorePage': True, 'canViewScorePageAuth': False, 'completeRequired': True, 'isActive': True, 'limitByScheduleFinish': False, 'limitByScheduleStart': True, 'onlyRegistered': False, 'randomSequences': True, 'viewAnswerKey': True, 'viewDetail': True, 'viewScore': True}, null=True),
        ),
    ]
