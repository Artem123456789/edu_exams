# Generated by Django 4.0.6 on 2023-03-25 16:04

from django.db import migrations, models
import django.db.models.deletion
import exams.contants
import exams.utils.file_upload
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_ordinaryquestionfilemodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrdinaryQuestionFileModel',
            new_name='OrdinaryQuestionFile',
        ),
        migrations.CreateModel(
            name='OrdinaryQuestionAnswerFile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'TYPE_IMAGE')], default=exams.contants.FileType['TYPE_IMAGE'])),
                ('file', models.FileField(upload_to=exams.utils.file_upload.file_ordinary_answer_upload)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='exams.ordinaryquestionanswer')),
            ],
            options={
                'verbose_name': 'Файл ответа на обычный вопрос',
                'verbose_name_plural': 'Файлы ответов на обычные вопрос',
            },
        ),
        migrations.CreateModel(
            name='ComparisonQuestionOptionFile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'TYPE_IMAGE')], default=exams.contants.FileType['TYPE_IMAGE'])),
                ('file', models.FileField(upload_to=exams.utils.file_upload.file_comparison_option_upload)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='exams.comparisonquestionoption')),
            ],
            options={
                'verbose_name': 'Файл опции вопроса с сопоставлением',
                'verbose_name_plural': 'Файлы опций вопросов с сопоставлением',
            },
        ),
        migrations.CreateModel(
            name='ComparisonQuestionOptionAnswerFile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'TYPE_IMAGE')], default=exams.contants.FileType['TYPE_IMAGE'])),
                ('file', models.FileField(upload_to=exams.utils.file_upload.file_comparison_option_answer_upload)),
                ('option_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='exams.comparisonquestionoptionanswer')),
            ],
            options={
                'verbose_name': 'Файл ответа на опцию вопроса с сопоставлением',
                'verbose_name_plural': 'Файлы ответов на опции вопросов с сопоставлением',
            },
        ),
        migrations.CreateModel(
            name='ComparisonQuestionFile',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'TYPE_IMAGE')], default=exams.contants.FileType['TYPE_IMAGE'])),
                ('file', models.FileField(upload_to=exams.utils.file_upload.file_comparison_question_upload)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='exams.comparisonquestion')),
            ],
            options={
                'verbose_name': 'Файл вопроса с сопоставлением',
                'verbose_name_plural': 'Файлы вопросов с сопоставлением',
            },
        ),
    ]