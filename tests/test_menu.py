# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from aldryn_apphooks_config.utils import get_app_instance

from django.utils.translation import activate
from menus.menu_pool import menu_pool
from parler.utils.context import switch_language, smart_override

from djangocms_blog.views import CategoryEntriesView, PostDetailView

from . import BaseTest


class MenuTest(BaseTest):
    cats = []

    def setUp(self):
        super(MenuTest, self).setUp()
        self.cats = [self.category_1]
        for i, lang_data in enumerate(self._categories_data):
            cat = self._get_category(lang_data['en'])
            if 'it' in lang_data:
                cat = self._get_category(lang_data['it'], cat, 'it')
            self.cats.append(cat)

        activate('en')
        menu_pool.discover_menus()
        # All cms menu modifiers should be removed from menu_pool.modifiers
        # so that they do not interfere with our menu nodes
        menu_pool.modifiers = [m for m in menu_pool.modifiers if m.__module__.startswith('djangocms_blog')]

    def test_menu_nodes(self):
        """
        Tests if all categories are present in the menu
        """
        self.get_posts()
        self.get_pages()

        for lang in ('en', 'it'):
            request = self.get_page_request(None, self.user, r'/%s/page-two/' % lang)
            with smart_override(lang):
                nodes = menu_pool.get_nodes(request, namespace='BlogCategoryMenu')
                nodes_url = set([node.url for node in nodes])
                cats_url = set([cat.get_absolute_url() for cat in self.cats if cat.has_translation(lang)])
                self.assertTrue(cats_url.issubset(nodes_url))

    def test_modifier(self):
        """
        Tests if correct category is selected in the menu
        according to context (view object)
        """
        posts = self.get_posts()
        pages = self.get_pages()

        tests = (
            # view class, view kwarg, view object, category
            (PostDetailView, 'slug', posts[0], posts[0].categories.first()),
            (CategoryEntriesView, 'category', self.cats[2], self.cats[2])
        )
        for view_cls, kwarg, obj, cat in tests:
            request = self.get_page_request(pages[1], self.user, path=obj.get_absolute_url())
            with smart_override('en'):
                with switch_language(obj, 'en'):
                    view_obj = view_cls()
                    view_obj.request = request
                    view_obj.namespace, view_obj.config = get_app_instance(request)
                    view_obj.app_config = self.app_config_1
                    view_obj.kwargs = {kwarg: obj.slug}
                    view_obj.get(request)
                    # check if selected menu node points to cat
                    nodes = menu_pool.get_nodes(request, namespace='BlogCategoryMenu')
                    found = False
                    for node in nodes:
                        if node.selected:
                            self.assertEqual(node.url, obj.get_absolute_url())
                            found = True
                            break
                    self.assertTrue(found)