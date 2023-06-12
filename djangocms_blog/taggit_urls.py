# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.urls import include, path

urlpatterns = [
    path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
]
