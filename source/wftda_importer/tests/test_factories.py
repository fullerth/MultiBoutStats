from django.test import TestCase

from wftda_importer.factories import RosterWithPlayersFactory, PlayerFactory, \
CompleteBoutFactory

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

        self.assertNotEqual(bout.home_roster, None)


