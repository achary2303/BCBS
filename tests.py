# pages/tests.py
from django.http import HttpRequest
from django.test import SimpleTestCase
#from django.urls import reverse

#from . import views
#from hash


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = selfs.client.get('/')
        self.assertEqual(response.statuxs_code, 200)