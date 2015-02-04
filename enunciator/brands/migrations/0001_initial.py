# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
import datetime

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('status', model_utils.fields.StatusField(no_check_for_status=True, default='draft', verbose_name='status', max_length=100, choices=[('draft', 'draft'), ('published', 'published')])),
                ('status_changed', model_utils.fields.MonitorField(monitor='status', default=django.utils.timezone.now, verbose_name='status changed')),
                ('name', models.CharField(help_text='Limited to 200 characters', default='', max_length=200)),
                ('slug', models.SlugField(unique=True, default='', help_text='Populates from the name field')),
                ('created', models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())),
                ('description', models.TextField(help_text='Plain text only', default='')),
                ('website', models.URLField(help_text='Optional', default='', blank=True)),
                ('logo', models.ImageField(help_text='Please use jpg (jpeg) or png files only', upload_to='brands/logos', default='')),
                ('vine_url', models.URLField(help_text='Paste the full URL to the individual Vine video (e.g. https://vine.co/v/bEjAgXjnzAW)', default='', blank=True)),
                ('video_url', models.URLField(help_text='Will populate when the brand is saved', default='', blank=True)),
                ('video', models.FileField(help_text='Will populate when the brand is saved', upload_to='brands/videos', default='', blank=True)),
                ('video_thumbnail_url', models.URLField(help_text='Will populate when the brand is saved', default='', blank=True)),
                ('video_thumbnail', models.ImageField(help_text='Will populate when brand is saved', upload_to='brands/video_thumbnails', default='', blank=True)),
            ],
            options={
                'ordering': ['created'],
            },
            bases=(models.Model,),
        ),
    ]
