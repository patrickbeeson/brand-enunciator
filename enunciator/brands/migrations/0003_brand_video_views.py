# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_auto_20150206_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='video_views',
            field=models.PositiveIntegerField(null=True, blank=True, default=0),
            preserve_default=True,
        ),
    ]
