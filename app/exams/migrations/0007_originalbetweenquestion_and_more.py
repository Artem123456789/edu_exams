# Generated by Django 4.0.6 on 2023-04-22 13:57

import app.exams.contants
import app.exams.utils.file_upload
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_originalquestion_originalquestionuseranswer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalBetweenQuestion',
            fields=[
                ('header', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.exam')),
            ],
            options={
                'verbose_name': 'Вопрос с вписыванием между текстом',
                'verbose_name_plural': 'Вопросы со вписыванием между текстом',
            },
        ),
        migrations.CreateModel(
            name='OriginalQuestionBetweenAnswerItem',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('text_answer', models.TextField(blank=True, null=True)),
                ('right_answer_points', models.SmallIntegerField(null=True)),
                ('order_index', models.SmallIntegerField(null=True)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.originalbetweenquestion')),
            ],
            options={
                'verbose_name': 'Элемент вопроса со вписыванием между текстом',
                'verbose_name_plural': 'Элементы вопросов со вписыванием между текстом',
            },
        ),
        migrations.CreateModel(
            name='OriginalQuestionBetweenUserAnswer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.originalquestionbetweenansweritem')),
                ('student_exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='exams.studentexam')),
            ],
            options={
                'verbose_name': 'Ответ пользователя на элемент вопроса со вписыванием между текстом',
                'verbose_name_plural': 'Ответы пользователей на элементы вопросов со вписыванием между текстом',
            },
        ),
        migrations.CreateModel(
            name='OriginalBetweenQuestionFile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'TYPE_IMAGE')], default=app.exams.contants.FileType['TYPE_IMAGE'])),
                ('file', models.FileField(upload_to=app.exams.utils.file_upload.file_original_between_question_upload)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='exams.originalbetweenquestion')),
            ],
            options={
                'verbose_name': 'Файл вопроса с вписыванием между текстом',
                'verbose_name_plural': 'Файлы вопросов с вписыванием между текстом',
            },
        ),
    ]
