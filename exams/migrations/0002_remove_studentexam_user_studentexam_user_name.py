# Generated by Django 4.0.6 on 2023-03-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentexam',
            name='user',
        ),
        migrations.AddField(
            model_name='studentexam',
            name='user_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
