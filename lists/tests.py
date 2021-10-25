from django.test import TestCase
from lists.views import home_page
from django.urls import resolve

class HomePageTests(TestCase):

    def test_root_urls_resloves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)