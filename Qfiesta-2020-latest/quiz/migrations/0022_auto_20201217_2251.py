# Generated by Django 2.1.5 on 2020-12-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0021_question_my_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hint',
            name='hint1',
        ),
        migrations.RemoveField(
            model_name='hint',
            name='hint2',
        ),
        migrations.RemoveField(
            model_name='hint',
            name='hint3',
        ),
        migrations.AddField(
            model_name='hint',
            name='HintPenalty',
            field=models.CharField(choices=[('1', 'hint 1'), ('2', 'hint 2'), ('3', 'hint 3')], max_length=10, null='true'),
            preserve_default='true',
        ),
        migrations.AddField(
            model_name='hint',
            name='Ishinttaken',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hint',
            name='hinttext',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='my_field',
            field=models.CharField(choices=[('audio', 'audio'), ('video', 'video'), ('image', 'image'), ('none', 'none')], max_length=10, null='true'),
        ),
    ]
