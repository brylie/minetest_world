from django.contrib import admin
from .models import Creation

# Register your models here.
class CreationAdmin(admin.ModelAdmin):
    fields = ['name', 'cover_photo', 'description', 'file', 'license']

admin.site.register(Creation, CreationAdmin)
