# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-06-23 09:44
from __future__ import unicode_literals

import aldryn_apphooks_config.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('djangocms_blog', '0041_auto_20171003_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='MostReadPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_blog_mostreadplugin', serialize=False, to='cms.CMSPlugin')),
                ('current_site', models.BooleanField(default=True, help_text='Select items from the current site only', verbose_name='current site')),
                ('template_folder', models.CharField(choices=[('plugins', 'Default template')], default='plugins', help_text='Select plugin template to load for this instance', max_length=200, verbose_name='Plugin template')),
                ('most_read_posts', models.IntegerField(default=5, help_text='The number of latests articles to be displayed.', verbose_name='articles')),
                ('app_config', aldryn_apphooks_config.fields.AppHookConfigField(blank=True, help_text='When selecting a value, the form is reloaded to get the updated default', null=True, on_delete=django.db.models.deletion.CASCADE, to='djangocms_blog.BlogConfig', verbose_name='app. config')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
