# Generated by Django 4.0.6 on 2023-03-23 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0004_comparisonquestionoption_right_answer_points_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comparisonquestionoptionanswer',
            name='option',
        ),
        migrations.AddField(
            model_name='comparisonquestionoption',
            name='option_answer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.comparisonquestionoptionanswer'),
        ),
    ]
