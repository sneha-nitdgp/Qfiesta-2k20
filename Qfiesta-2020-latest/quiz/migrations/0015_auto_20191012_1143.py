# Generated by Django 2.0.5 on 2019-10-12 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20191012_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='rounds',
            new_name='round',
        ),
    ]
