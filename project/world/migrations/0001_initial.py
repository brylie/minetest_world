# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import world.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('cover_photo', models.ImageField(blank=True, upload_to=world.models.image_upload_location)),
                ('license', models.CharField(choices=[('CC-by', 'Creative Commons - Attribution'), ('CC-zero', 'Creative Commons Zero (Public Domain)')], default='CC-by', max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorldRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_file', models.FileField(upload_to=world.models.upload_location)),
                ('materials_file', models.FileField(upload_to=world.models.upload_location)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('world', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='world.World')),
            ],
        ),
    ]
