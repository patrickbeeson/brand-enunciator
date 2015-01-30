from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class BrandsTest(TestCase):

    def setUp(self):
        pass

    def test_get_brand(self):
        """Ensure we can get a brand"""
        url = reverse('brand-detail')
        client = Client()
        response = client.get(url)
        print(response.content)
