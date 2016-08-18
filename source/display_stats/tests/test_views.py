from django.core.urlresolvers import reverse

from django.test import TestCase
from django.test.client import Client

from wftda_importer.models import Player, Jam, PlayerToJam

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

    def test_stat_page_passes_num_jams_in_context(self):
        """Ensure num_jams contains the correct total jams for a player"""
        expected_jams = 5

        p = Player.objects.create()

        for i in range(0, expected_jams):
            j = Jam.objects.create()
            PlayerToJam.objects.create(player=p, jam=j)

        c = Client()
        response = c.get(reverse(self.test_url))
        self.assertEqual(expected_jams, response.context['num_jams'])

    def test_stat_page_passes_total_jams_in_context(self):
        """Ensure total_jams contains the correct total available jams"""
        expected_jams = 10

        p = Player.objects.create()

        for i in range(0, expected_jams):
            j = Jam.objects.create()
        
        c = Client()
        response = c.get(reverse(self.test_url))
        self.assertEqual(expected_jams, response.context['total_jams'])

    def test_stat_page_passes_blocker_jams_in_context(self):
        """Ensure blocker_jams contains the correct jams blocked by the player"""
        expected_jams = 12

        p = Player.objects.create()

        for i in range(0, expected_jams):
            j = Jam.objects.create()
            PlayerToJam.objects.create(player = p, jam = j)


