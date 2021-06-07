# Generated by Django 3.1.1 on 2020-12-07 22:51

import Test.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answerID', models.CharField(default=Test.models.Answer.generate_id, max_length=16, unique=True)),
                ('testTakerID', models.CharField(max_length=16)),
                ('session_key', models.CharField(max_length=16)),
                ('testID', models.CharField(max_length=16)),
                ('questionID', models.CharField(max_length=16)),
                ('num_ofAnswer', models.IntegerField(default=0)),
                ('answer', models.CharField(max_length=4096)),
                ('scoreObtain', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questID', models.CharField(default='9ede09a07d76282b', max_length=16)),
                ('questionNum', models.IntegerField(default=0)),
                ('question', models.TextField()),
                ('testID', models.CharField(max_length=16)),
                ('answerKey', models.CharField(max_length=1024)),
                ('choiceFirst', models.TextField()),
                ('choiceSecond', models.TextField(blank=True, default=None, null=True)),
                ('choiceThird', models.TextField(blank=True, default=None, null=True)),
                ('choiceFourth', models.TextField(blank=True, default=None, null=True)),
                ('choiceFifth', models.TextField(blank=True, default=None, null=True)),
                ('choiceSixth', models.TextField(blank=True, default=None, null=True)),
                ('nextQuestID', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('prevQuestID', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('trueScore', models.IntegerField(default=0)),
                ('falseScore', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TestPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testID', models.CharField(default='05cf8a6f7a68d46b', max_length=16)),
                ('testTitle', models.CharField(max_length=1024)),
                ('testAuthor', models.CharField(max_length=1024)),
                ('questionCount', models.CharField(default=0, max_length=4)),
                ('testCode', models.CharField(default=None, max_length=6)),
                ('testSchedule', models.DateField()),
                ('timeLimit', models.IntegerField(default=0, null=True)),
                ('passwordAdminTest', models.CharField(default=None, max_length=16, null=True)),
                ('passwordTest', models.CharField(default='123456', max_length=16)),
                ('firstQuestID', models.CharField(blank=True, default=None, max_length=16, null=True)),
                ('maxScore', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TestTaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testTakerID', models.CharField(default='074c81c7416cdc41', max_length=16, unique=True)),
                ('session_key', models.CharField(max_length=16)),
                ('session_password', models.CharField(max_length=16)),
                ('testID', models.CharField(max_length=16)),
                ('testTakerName', models.CharField(max_length=128)),
                ('testTakerGroup', models.CharField(blank=True, max_length=128, null=True)),
                ('scoreObtained', models.IntegerField(default=0)),
                ('lastAnswered', models.IntegerField(default=0)),
            ],
        ),
    ]
