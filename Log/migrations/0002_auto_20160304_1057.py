# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log_list',
            old_name='log_Name',
            new_name='log_content',
        ),
        migrations.AddField(
            model_name='log_list',
            name='log_name',
            field=models.CharField(default=datetime.datetime(2016, 3, 4, 3, 57, 0, 179823, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
