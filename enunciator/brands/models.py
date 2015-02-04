import requests
import datetime
import os
import logging
import urllib

from model_utils.models import StatusModel
from model_utils import Choices

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.core.urlresolvers import reverse

from enunciator.utils.validators import validate_file_type

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
        unique=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    description = models.TextField(
        default='',
        help_text='Plain text only',
    )
    website = models.URLField(
        default='',
        help_text='Optional',
        blank=True,
    )
    logo = models.ImageField(
        upload_to='brands/logos',
        default='',
        help_text='Please use jpg (jpeg) or png files only',
        validators=[validate_file_type],
    )
    vine_url = models.URLField(
        default='',
        help_text='Paste the full URL to the individual Vine video (e.g. https://vine.co/v/bEjAgXjnzAW)',
        blank=True,
    )
    video_url = models.URLField(
        default='',
        blank=True,
        help_text='Will populate when the brand is saved',
    )
    video = models.FileField(
        upload_to='brands/videos',
        default='',
        blank=True,
        help_text='Will populate when the brand is saved',
        validators=[validate_file_type],
    )
    video_thumbnail_url = models.URLField(
        default='',
        blank=True,
        help_text='Will populate when the brand is saved',
    )
    video_thumbnail = models.ImageField(
        upload_to='brands/video_thumbnails',
        default='',
        blank=True,
        help_text='Will populate when brand is saved',
        validators=[validate_file_type],
    )

    class Meta:
        ordering = ['created']

    def get_remote_image(self):
        if self.video_thumbnail_url and not self.video_thumbnail:
            local_tn, headers = urllib.request.urlretrieve(self.video_thumbnail_url)
            with open(local_tn, 'rb') as tn:
                self.video_thumbnail.save(
                    os.path.basename(self.slug).split('?')[0],
                    File(tn)
                )
            self.save()

    def get_remote_video(self):
        if self.video_url and not self.video:
            local_video, headers = urllib.request.urlretrieve(self.video_url)
            with open(local_video, 'rb') as video:
                self.video.save(
                    os.path.basename(self.slug).split('?')[0],
                    File(video)
                )
            self.save()

    def save(self, *args, **kwargs):
        """
        Set the video url, thumbnail url and thumnail values from Vine API
        """
        if self.vine_url:
            # Split the video ID from the vine URL provided
            vine_video_id = os.path.split(self.vine_url)[1:]
            # Construct the API path for the video
            vine_api_path = os.path.join(
                'https://api.vineapp.com/timelines/posts/s/',
                vine_video_id[0]
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
                    # Assign the video_url value from JSON
                    self.video_url = r_json['data']['records'][0]['videoUrl']
                    # Assign the video_thumbnail_url from JSON
                    self.video_thumbnail_url = r_json['data']['records'][0]['thumbnailUrl']
            except ConnectionError:
                logger.error('There was a problem connecting to Vine.')
        super(Brand, self).save(*args, **kwargs)
        self.get_remote_video()
        self.get_remote_image()

    def __str__(self):
        return '{}'.format(self.name)
