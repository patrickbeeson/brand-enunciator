import requests
import datetime
import os
import logging

from model_utils.models import StatusModel
from model_utils import Choices

from django.db import models
from django.core.urlresolvers import reverse

logger = logging.getLogger(__name__)


class Brand(StatusModel):
    """
    A brand to enunciate
    """
    STATUS = Choices('draft', 'published')
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
    created = models.DateTimeField(
        auto_now_add=True,
        default=''
    )
    description = models.TextField(
        default='',
        help_text='Plain text only'
    )
    website = models.URLField(
        default='',
        help_text='Optional',
        blank=True
    )
    logo = models.ImageField(
        upload_to='brands/logos',
        default='',
        help_text='Please use jpg (jpeg) or png files only'
        # TODO add validator
    )
    vine_url = models.URLField(
        default='',
        help_text='Paste the full URL to the individual Vine video (e.g. https://vine.co/v/bEjAgXjnzAW)',
        blank=True
    )
    video_url = models.URLField(
        default='',
        blank=True,
        help_text='Will populate when the brand is saved'
    )
    video_thumbnail_url = models.URLField(
        default='',
        blank=True,
        help_text='Will populate when the brand is saved'
    )

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse('brands.views.detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        """Set the video url and thumbnail url values from Vine API"""
        # Split the video ID from the vine URL provided
        vine_video_id = os.path.split(self.vine_url)[1:]
        # Construct the API path for the video
        vine_api_path = os.path.join(
            'https://api.vineapp.com/timelines/posts/s/',
            vine_video_id
        )
        try:
            # Build the request for our JSON object
            r = requests.get(vine_api_path)
            # Abort if we don't get a 200 code
            if r.status_code != 200:
                logger.error(
                    'There was a problem fetching the video ID {}'.format(
                        vine_video_id
                    )
                )
                return
            else:
                r_json = r.json()
                self.video_url = r_json['data']['records'][0]['videoUrl']
                self.video_thumbnail_url = r_json['data']['records'][0]['thumbnailUrl']
                super(Brand, self).save(*args, **kwargs)
        except ConnectionError:
            logger.error('There was a problem connecting to Vine.')

    def __str__(self):
        return '{}'.format(self.name)
