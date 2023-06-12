# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.urls import path, re_path

from djangocms_blog.feeds import FBInstantArticles, LatestEntriesFeed, TagFeed
from djangocms_blog.settings import get_setting
from djangocms_blog.views import (
    AuthorEntriesView, CategoryEntriesView, PostArchiveView, PostDetailView, PostListView,
    TaggedListView,
)


def get_urls():
    urls = get_setting('PERMALINK_URLS')
    details = []
    for urlconf in urls.values():
        details.append(
            re_path(urlconf, PostDetailView.as_view(), name='post-detail'),
        )
    return details


detail_urls = get_urls()

urlpatterns = [
    path('latests/',
        PostListView.as_view(), name='posts-latest'),
    path('feed/',
        LatestEntriesFeed(), name='posts-latest-feed'),
    path('feed/fb/',
        FBInstantArticles(), name='posts-latest-feed-fb'),
    re_path(r'^(?P<year>\d{4})/$',
        PostArchiveView.as_view(), name='posts-archive'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        PostArchiveView.as_view(), name='posts-archive'),
    re_path(r'^author/(?P<username>[\w\.@+-]+)/$',
        AuthorEntriesView.as_view(), name='posts-author'),
    re_path(r'^category/(?P<category>[\w\.@+-]+)/$',
        CategoryEntriesView.as_view(), name='posts-category'),
    re_path(r'^tag/(?P<tag>[-\w]+)/$',
        TaggedListView.as_view(), name='posts-tagged'),
    re_path(r'^tag/(?P<tag>[-\w]+)/feed/$',
        TagFeed(), name='posts-tagged-feed'),
] + detail_urls
