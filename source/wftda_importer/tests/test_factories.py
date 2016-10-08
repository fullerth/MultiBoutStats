from django.test import TestCase

from wftda_importer.factories import RosterWithPlayersFactory, PlayerFactory, \
CompleteBoutFactory

from wftda_importer.models import Jam

class TestRosterWithPlayersFactory(TestCase):
    def test_creates_and_adds_players(self):
        roster = RosterWithPlayersFactory()
        
        self.assertNotEqual(roster.players.count(), 0, 
            msg="RosterWithPlayersFactory should create and add some players")
    def test_adds_players_from_argument(self):
        player_list = [PlayerFactory(), PlayerFactory()]

        roster = RosterWithPlayersFactory(players=player_list)

        self.assertListEqual(list(roster.players.all()), player_list)

class TestCompleteBoutFactory(TestCase):
    def test_creates_and_adds_rosters_with_players(self):
        bout = CompleteBoutFactory()
 
        with self.subTest(msg="Home Roster is not set"):
            self.assertNotEqual(bout.home_roster, None)

        self.assertNotEqual(0, Jam.objects.all().count())




