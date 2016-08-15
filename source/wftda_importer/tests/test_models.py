from django.test import TestCase

from wftda_importer.models import Player, Jam

class PlayerTests(TestCase):
    def setUp(self):
        pass

    def test_model_can_store_name(self):
        p = Player(name="Thump R. Dickhoff")

class JamTests(TestCase):
    def test_model_can_store_players(self):
        p = Player.objects.create()
        j = Jam.objects.create()
        j.players.add(p)

        
