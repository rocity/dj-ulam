# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
