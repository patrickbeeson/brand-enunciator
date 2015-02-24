# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_brand_video_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='tagline',
            field=models.CharField(default='', help_text='Plain text only. Limited to 200 characters.', max_length=200),
            preserve_default=True,
        ),
    ]
