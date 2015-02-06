# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import enunciator.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(upload_to='brands/logos', help_text='Please use jpg (jpeg) or png files only', default='', validators=[enunciator.utils.validators.validate_file_type]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brand',
            name='video',
            field=models.FileField(max_length=200, upload_to='brands/videos', help_text='Will populate when the brand is saved', validators=[enunciator.utils.validators.validate_file_type], blank=True, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brand',
            name='video_thumbnail',
            field=models.ImageField(max_length=200, upload_to='brands/video_thumbnails', help_text='Will populate when brand is saved', validators=[enunciator.utils.validators.validate_file_type], blank=True, default=''),
            preserve_default=True,
        ),
    ]
