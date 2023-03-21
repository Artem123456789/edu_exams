# Generated by Django 4.0.6 on 2023-03-21 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComparisonQuestion',
            fields=[
                ('header', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ComparisonQuestionOption',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.comparisonquestion')),
            ],
        ),
        migrations.CreateModel(
            name='ComparisonQuestionOptionAnswer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('option', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.comparisonquestionoption')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrdinaryQuestion',
            fields=[
                ('header', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.exam')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrdinaryQuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField()),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.ordinaryquestion')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.school')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentExam',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.exam')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrdinaryQuestionUserAnswer',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.ordinaryquestionanswer')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.ordinaryquestion')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.subject'),
        ),
        migrations.CreateModel(
            name='ComparisonQuestionUserAnswer',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.comparisonquestionoption')),
                ('option_answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.comparisonquestionoptionanswer')),
                ('student_exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.studentexam')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comparisonquestion',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.exam'),
        ),
    ]