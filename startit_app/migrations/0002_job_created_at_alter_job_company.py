# Generated by Django 5.1.1 on 2024-10-11 05:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=100, verbose_name='Название компании'),
        ),
    ]