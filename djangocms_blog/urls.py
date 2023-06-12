# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.urls import path, re_path
from django.utils.translation import gettext_lazy as _
from .feeds import FBInstantArticles, LatestEntriesFeed, TagFeed
from .settings import get_setting
from .views import (
    AuthorEntriesView, CategoryEntriesView, PostArchiveView, PostDetailView, PostListView,
    TaggedListView, MostReadPostsView, RecommendedPostsView, FavouritesPostsView, PostAutocomplete,
    copy_language)


def get_urls():
    urls = get_setting('PERMALINK_URLS')
    details = []
    for urlconf in urls.values():
        details.append(
            re_path(urlconf, PostDetailView.as_view(), name='post-detail'),
        )
    return details


detail_urls = get_urls()

# module-level app_name attribute as per django 1.9+
app_name = 'djangocms_blog'
urlpatterns = [
    path('',
        PostListView.as_view(), name='posts-latest'),
    re_path(_(r'^all/$'),
        PostListView.as_view(), name='posts-latest-all'),
    re_path(_(r'^most_read/$'),
        MostReadPostsView.as_view(), name='posts-most-read'),
    re_path(_(r'^recommended/$'),
        RecommendedPostsView.as_view(), name='posts-recommended'),
    re_path(_(r'^newest/$'),
        FavouritesPostsView.as_view(), name='posts-newest'),
    re_path(_(r'^feed/$'),
        LatestEntriesFeed(), name='posts-latest-feed'),
    re_path(_(r'^feed/fb/$'),
        FBInstantArticles(), name='posts-latest-feed-fb'),
    re_path(_(r'^(?P<year>\d{4})/$'),
        PostArchiveView.as_view(), name='posts-archive'),
    re_path(_(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$'),
        PostArchiveView.as_view(), name='posts-archive'),
    re_path(_(r'^author/(?P<username>[\w\.@+-]+)/$'),
        AuthorEntriesView.as_view(), name='posts-author'),
    re_path(_(r'^category/(?P<category>[\w\.@+-]+)/$'),
        CategoryEntriesView.as_view(), name='posts-category'),
    re_path(_(r'^tag/(?P<tag>[-\w]+)/$'),
        TaggedListView.as_view(), name='posts-tagged'),
    re_path(_(r'^tag/(?P<tag>[-\w]+)/feed/$'),
        TagFeed(), name='posts-tagged-feed'),
    path('copy_language/<int:post_id>', copy_language, name='copy-language-blog'),
    path('post-autocomplete/', PostAutocomplete.as_view(), name='post-autocomplete', ),
] + detail_urls
