# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from .feeds import FBInstantArticles, LatestEntriesFeed, TagFeed
from .settings import get_setting
from .views import (
    AuthorEntriesView, CategoryEntriesView, PostArchiveView, PostDetailView, PostListView,
    TaggedListView, MostReadPostsView, RecommendedPostsView, FavouritesPostsView,
    copy_language)


def get_urls():
    urls = get_setting('PERMALINK_URLS')
    details = []
    for urlconf in urls.values():
        details.append(
            url(urlconf, PostDetailView.as_view(), name='post-detail'),
        )
    return details


detail_urls = get_urls()

# module-level app_name attribute as per django 1.9+
app_name = 'djangocms_blog'
urlpatterns = [
    url(r'^$',
        PostListView.as_view(), name='posts-latest'),
    url(_(r'^all/$'),
        PostListView.as_view(), name='posts-latest-all'),
    url(_(r'^most_read/$'),
        MostReadPostsView.as_view(), name='posts-most-read'),
    url(_(r'^recommended/$'),
        RecommendedPostsView.as_view(), name='posts-recommended'),
    url(_(r'^newest/$'),
        FavouritesPostsView.as_view(), name='posts-newest'),
    url(_(r'^feed/$'),
        LatestEntriesFeed(), name='posts-latest-feed'),
    url(_(r'^feed/fb/$'),
        FBInstantArticles(), name='posts-latest-feed-fb'),
    url(_(r'^(?P<year>\d{4})/$'),
        PostArchiveView.as_view(), name='posts-archive'),
    url(_(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$'),
        PostArchiveView.as_view(), name='posts-archive'),
    url(_(r'^author/(?P<username>[\w\.@+-]+)/$'),
        AuthorEntriesView.as_view(), name='posts-author'),
    url(_(r'^category/(?P<category>[\w\.@+-]+)/$'),
        CategoryEntriesView.as_view(), name='posts-category'),
    url(_(r'^tag/(?P<tag>[-\w]+)/$'),
        TaggedListView.as_view(), name='posts-tagged'),
    url(_(r'^tag/(?P<tag>[-\w]+)/feed/$'),
        TagFeed(), name='posts-tagged-feed'),
    url(r'^copy_language/(?P<post_id>\d+)$', copy_language, name='copy-language-blog'),
] + detail_urls
