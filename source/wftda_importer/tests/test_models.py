from django.test import TestCase

from wftda_importer.models import Player, Jam

class PlayerTests(TestCase):
    def setUp(self):
        pass

    def test_model_can_store_name(self):
        p = Player(name="Thump R. Dickhoff")

class JamTests(TestCase):
    pass
