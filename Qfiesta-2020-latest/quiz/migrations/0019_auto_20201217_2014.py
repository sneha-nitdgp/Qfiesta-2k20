# Generated by Django 2.1.5 on 2020-12-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0018_hint'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='my_field',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='image',
            name='my_field',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='my_field',
            field=models.BooleanField(default=False),
        ),
    ]
