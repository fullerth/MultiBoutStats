from django.core.urlresolvers import reverse

from django.test import TestCase
from django.test.client import Client


from wftda_importer.models import Player

class StatDisplayPageTest(TestCase):
    def setUp(self):
        pass

    def test_page_exists(self):
        '''
        '''
        c = Client()
        response = c.get(reverse('display_stats'))
        
        self.assertTemplateUsed(response, 'wftda_importer/stat_display.html')
        
