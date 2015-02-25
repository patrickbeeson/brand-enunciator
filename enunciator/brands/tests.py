from rest_framework.test import APIClient
import factory
import datetime

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from brands.models import Brand


class BrandFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Brand
    status = 'published'
    status_changed = datetime.datetime.now()
    tagline = 'The greatest brand ever.'
    description = 'My brand description'
    logo = factory.django.ImageField(format='JPEG')


class BrandsTest(TestCase):

    def setUp(self):
        self.brand_1 = BrandFactory.create(name='Brand 1', slug='brand-1')

    def tearDown(self):
        self.brand_1.delete()

    def test_get_brand(self):
        self.assertEqual(self.brand_1.name, 'Brand 1')


class BrandApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.brand_1 = BrandFactory.create(name='Brand 1', slug='brand-1')
        self.brand_2 = BrandFactory.create(name='Brand 2', slug='brand-2')

    def tearDown(self):
        self.brand_1.delete()
        self.brand_2.delete()

    def test_get_individual_brand(self):
        response = self.client.get(reverse('brand-detail', kwargs={'slug': 'brand-1'}))
        self.assertEqual(response.status_code, 200)

    def test_get_individual_brand(self):
        response = self.client.get(reverse('brand-list'))
        self.assertEqual(response.status_code, 200)

    def test_patch_brand_video_views(self):
        url = reverse('brand-detail', kwargs={'slug': 'brand-1'})
        data = {'video_views': 1}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.data['video_views'], data['video_views'])

    def test_cannot_patch_brand_attributes(self):
        url = reverse('brand-detail', kwargs={'slug': 'brand-1'})
        data = {'name': 'Brand 1000'}
        response = self.client.patch(url, data, format='json')
        self.assertNotEqual(response.data['name'], data['name'])
