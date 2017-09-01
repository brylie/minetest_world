from django.contrib import admin
from .models import World, WorldRevision

class WorldAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'cover_photo', 'license']

# Register your models here.
admin.site.register(World, WorldAdmin)
admin.site.register(WorldRevision)
