import os
from django.core.exceptions import ValidationError


def validate_file_type(value):
    accepted_extensions = ['.png', '.jpg', '.jpeg', '.mp4']
    extension = os.path.splitext(value.name)[1]
    if extension not in accepted_extensions:
        raise ValidationError(u'{} is not an accepted file type'.format(value))
