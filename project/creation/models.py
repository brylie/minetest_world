from django.db import models
from django.utils.text import slugify

# Create your models here.

def creation_upload_location(creation, filename):
    # put file in creations folder using slugified name
    return "creations/%s/%s" % (creation.slug, filename)

def image_upload_location(creation, filename):
    return "creations/%s/%s" % (creation.slug, filename)

class Creation(models.Model):
    LICENSE_CHOICES = (
        ('CC-by', 'Creative Commons - Attribution'),
        ('CC-zero', 'Creative Commons Zero (Public Domain)'),
    )

    LICENSE_DEFAULT = 'CC-by'

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    cover_photo = models.ImageField(upload_to=image_upload_location, blank=True)
    slug = models.SlugField(max_length=100)
    file = models.FileField(upload_to=creation_upload_location)
    license = models.CharField(
        max_length=7,
        choices=LICENSE_CHOICES,
        default=LICENSE_DEFAULT,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # automatically add slug when saving new world
    # https://stackoverflow.com/a/1480440/1191545
    def save(self, *args, **kwargs):
        # Make sure world does not already exist
        # to keep from breaking existing URLs
        if not self.id:
            self.slug = slugify(self.name)

        # Save the world!
        super(Creation, self).save(*args, **kwargs)

    def __str__(self):
        # Return creation name
        return self.name
