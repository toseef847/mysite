# Generated by Django 3.0.5 on 2020-04-25 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today),
        ),
    ]
