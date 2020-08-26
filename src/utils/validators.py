from django.core.exceptions import ValidationError
import os


def validate_file_size(value):
    filesize= value.size
    if filesize > 1000000:
        raise ValidationError("The maximum file size that can be uploaded is 1MB")
    else:
        return value

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[-1]
    valid_extensions = ['.png','.jpeg','.jpg']
    if not ext in valid_extensions:
        raise ValidationError('Only .jpeg, .jpg and .png are supported')