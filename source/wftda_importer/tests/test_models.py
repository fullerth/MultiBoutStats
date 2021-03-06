from django.core.urlresolvers import reverse
from django.test import TestCase

from wftda_importer.models import Player, Jam, PlayerToJam, Bout, Roster

from wftda_importer import factories

class PlayerTests(TestCase):
    def setUp(self):
        pass

    def test_model_can_store_name(self):
        p = Player(name="Thump R. Dickhoff")

    def test_model_str_method(self):
        expected_repr = "Cassie Beck"
        p = Player.objects.create(name="Cassie Beck")
        self.assertEqual(expected_repr, str(p))

class JamTests(TestCase):
    def test_model_fields_exist(self):
        p1 = Player.objects.create()
        p2 = Player.objects.create()
        bout = factories.BoutFactory()
        j = Jam.objects.create(bout=bout)
        PlayerToJam.objects.create(player=p1, jam=j)
        PlayerToJam.objects.create(player=p2, jam=j)

class PlayerToJamTests(TestCase):
    def test_model_fields_exist(self):
        p = Player.objects.create()
        j = Jam.objects.create()
        position = PlayerToJam.JAMMER
        lead_jammer = True

        PlayerToJam(player=p, jam=j, position=position, lead_flag=lead_jammer)

class BoutTests(TestCase):
    def test_model_fields_exist(self):
        expected_name = "Test Bout"
        expected_home_roster = Roster.objects.create()
        
        b = Bout.objects.create(location=expected_name, 
                home_roster=expected_home_roster)

    def test_model_string_representation(self):
        expected_location = "Rat's Nest"
        expected_string = "{0}".format(expected_location)

        b = Bout.objects.create(location=expected_string)

        self.assertEqual(str(b), expected_string)

class RosterTests(TestCase):
    def test_model_fields_exist(self):
        expected_players = [factories.PlayerFactory(), 
                factories.PlayerFactory(), factories.PlayerFactory()]

        roster = Roster.objects.create()

        for player in expected_players:
            roster.players.add(player)

        observed_players = list(roster.players.all())

        self.assertListEqual(expected_players, observed_players)

