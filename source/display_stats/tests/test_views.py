from django.core.urlresolvers import reverse

from django.test import TestCase
from django.test.client import Client

from wftda_importer.models import Player, Jam, PlayerToJam, Bout
from wftda_importer.factories import JamFactory, PlayerFactory, \
    PlayerToJamFactory, RosterWithPlayersFactory, BoutFactory

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

    def test_stat_page_passes_total_jams_available_in_context(self):
        """Ensure total_jams_available contains the available jams for player"""
        total_jams = 10
        available_jams = 5

        p = PlayerFactory()
        bout = BoutFactory() 
        bout.home_roster.players.add(p)

        for i in range(0, total_jams):
            if(i < available_jams):
                player = p
            else:
                player = None
            j = JamFactory(bout=bout)
            PlayerToJamFactory(player=player, jam=j)

        c = Client()
        response = c.get(reverse(self.test_url))
        self.assertEqual(total_jams, 
                response.context['total_jams_available'])

    def test_stat_page_passes_correct_jam_position_counts_in_context(self):
        """Ensure context contains the correct jam positions by the player"""
        expected_blocking = 4
        expected_jamming = 6
        expected_pivot = 3
        total_jams = expected_blocking + expected_jamming + expected_pivot

        p = Player.objects.create()
        p2 = Player.objects.create()

        for i in range(0, total_jams):
            j = Jam.objects.create()
            if(i < expected_blocking):
                PlayerToJam.objects.create(player = p, jam = j, 
                        position = PlayerToJam.BLOCKER)
            elif(i < (expected_blocking+expected_jamming)):
                PlayerToJam.objects.create(player = p, jam = j, 
                        position = PlayerToJam.JAMMER)
            elif(i < (expected_blocking+expected_jamming+expected_pivot)):
                PlayerToJam.objects.create(player = p, jam = j,
                        position = PlayerToJam.PIVOT)
            #Make sure only displaying info for current player
            PlayerToJam.objects.create(player = p2, jam = j, 
                    position = PlayerToJam.BLOCKER)
            PlayerToJam.objects.create(player = p2, jam = j, 
                    position = PlayerToJam.PIVOT)
            PlayerToJam.objects.create(player = p2, jam = j, 
                    position = PlayerToJam.JAMMER)

        c = Client()
        response = c.get(reverse(self.test_url))
        self.assertEqual(expected_blocking, response.context['blocker_jams'],
                msg="Incorrect blocking jams reported")
        self.assertEqual(expected_jamming, response.context['jammer_jams'],
                msg="Incorrect jamming jams reported")
        self.assertEqual(expected_pivot, response.context['pivot_jams'],
                msg="Incorrect pivot jams reported")

    def test_stat_page_passes_correct_bouts_played_in_context(self):
        """Ensure context contains correct number of bouts played by the player"""
        roster = RosterWithPlayersFactory()
        
        expected_bouts = 5
        for i in range(0, expected_bouts):
            Bout.objects.create(home_roster=roster)

        c = Client()
        response = c.get(reverse(self.test_url))
        self.assertEqual(expected_bouts, response.context['bouts_played'],
                msg="Incorrect bouts played in context")

