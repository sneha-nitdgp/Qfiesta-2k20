# Generated by Django 2.1.5 on 2020-12-17 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_auto_20201217_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint1', models.CharField(max_length=500)),
                ('hint2', models.CharField(max_length=500)),
                ('hint3', models.CharField(max_length=500)),
                ('Question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
            ],
        ),
    ]
