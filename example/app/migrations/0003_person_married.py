# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 14:02


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150328_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='married',
            field=models.BooleanField(default=False, verbose_name=b'married'),
        ),
    ]
