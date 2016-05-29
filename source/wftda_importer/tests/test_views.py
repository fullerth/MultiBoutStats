from django.core.urlresolvers import reverse

from django.test import TestCase
from django.test.client import Client

from wftda_importer.models import Player

class StatDisplayPageTest(TestCase):
    def setUp(self):
        pass

    def test_page_renders_with_correct_template(self):
        '''
        Ensure the correct template is used to display player statistics
        '''
        c = Client()
        response = c.get(reverse('display_stats'))
        self.assertTemplateUsed(response, 'wftda_importer/stat_display.html')
        
    def test_stat_page_passes_name_in_context(self):
        '''
        '''
        expected_name = "Luna"
        p = Player()
        p.name = expected_name
        c = Client()
        response = c.get(reverse('display_stats'))
        self.assertEqual(expected_name, response.context['name'])
