from django.core.urlresolvers import reverse

from django.test import TestCase
from django.test.client import Client

from wftda_importer.models import Player

class StatDisplayPageTest(TestCase):
    def setUp(self):
        self.test_url = 'display_stats'
        
    def test_page_renders_with_correct_template(self):
        """Ensure the correct template is used to display player statistics"""
        p = Player()
        p.save()

        c = Client()
        response = c.get(reverse(self.test_url))
        self.assertTemplateUsed(response, 'display_stats/display_stats.html')

    def test_stat_page_passes_name_in_context(self):
        """Ensure name:Player.name is passed in the detail page context"""
        expected_name = "Luna"
        p = Player()
        p.name = expected_name
        p.save()

        c = Client()
        response = c.get(reverse(self.test_url))
        self.assertEqual(expected_name, response.context['name'])

