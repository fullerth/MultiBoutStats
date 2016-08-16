from django.test import TestCase

from wftda_importer.models import Player, Jam

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
    def test_model_can_store_players(self):
        p1 = Player.objects.create()
        p2 = Player.objects.create()
        j = Jam.objects.create()
        j.players.add(p1)
        j.players.add(p2)

        
