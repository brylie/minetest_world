from django.db import models
from django.utils.text import slugify
import datetime

def image_upload_location(world, filename):
    return "worlds/%s/%s" % (world.slug, filename)

# Create your models here.
class World(models.Model):
    LICENSE_CHOICES = (
        ('CC-by', 'Creative Commons - Attribution'),
        ('CC-zero', 'Creative Commons Zero (Public Domain)'),
    )

    LICENSE_DEFAULT = 'CC-by'

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    cover_photo = models.ImageField(upload_to=image_upload_location, blank=True)
    license = models.CharField(
        max_length=7,
        choices=LICENSE_CHOICES,
        default=LICENSE_DEFAULT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100)

    # automatically add slug when saving new world
    # https://stackoverflow.com/a/1480440/1191545
    def save(self, *args, **kwargs):
        # Make sure world does not already exist
        # to keep from breaking existing URLs
        if not self.id:
            self.slug = slugify(self.name)

        # Save the world!
        super(World, self).save(*args, **kwargs)

    def __str__(self):
        # Return world name
        return self.name

def upload_location(instance, filename):
    # Get current date/time with year, month, day, hour, minute, second
    current_date = datetime.datetime.today().strftime('%Y-%m-%dT%H%M%S')

    return "worlds/%s/%s/%s" % (instance.world.slug, current_date, filename)

class WorldRevision(models.Model):
    world = models.ForeignKey(World)
    map_file = models.FileField(upload_to=upload_location)
    materials_file = models.FileField(upload_to=upload_location)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.world.name + ' revision'
