import requests

from django.db import models


class Brand(models.Model):
    """
    A brand object
    """
    name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters',
        default=''
    )
    slug = models.SlugField(
        help_text='Populates from the name field',
        default='',
        unique=True
    )
    description = models.TextField(
        default=''
    )
    website = models.URLField(
        default=''
    )
    logo = models.ImageField(
        upload_to='brands/logos',
        default='',
        help_text='Please use jpg (jpeg) or png files only'
        # TODO add validator
    )
    vine_url = models.URLField(
        default=''
    )
    video_url = models.URLField(
        default=''
    )
    video_thumbnail_url = models.URLField(
        default=''
    )
