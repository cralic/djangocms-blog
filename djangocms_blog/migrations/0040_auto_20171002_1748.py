# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-02 15:48
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0039_post_pinned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='main_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image', verbose_name='Blog category image'),
        ),
    ]
