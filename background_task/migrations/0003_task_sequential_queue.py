# Generated by Django 2.1 on 2020-04-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('background_task', '0002_auto_20170927_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='sequential_queue',
            field=models.BooleanField(default=False),
        ),
    ]
