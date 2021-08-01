# Generated by Django 2.0.5 on 2019-08-21 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20190819_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('ans', models.CharField(default=None, max_length=500)),
                ('hint', models.CharField(default=None, max_length=500)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Rounds')),
            ],
        ),
        migrations.RemoveField(
            model_name='questions',
            name='rounds',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='currRounnd',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]