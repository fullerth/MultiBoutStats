from django.test import TestCase

from wftda_importer.factories import RosterWithPlayersFactory, PlayerFactory, \
CompleteBoutFactory

from wftda_importer.models import Jam, Player

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

        with self.subTest(msg="Jam object is not created"):
            self.assertNotEqual(0, Jam.objects.all().count())

        with self.subTest(msg="Players were not created"):
            self.assertNotEqual(0, Player.objects.all().count())

        with self.subTest(msg="Players not placed in jams"):
            #Jams cannot happen without at least one player
            self.assertEqual(0, Jam.objects.filter(
                players__isnull=True).count())

        with self.subTest(msg="Jam not added to the bout"):
            #Bouts cannot happen without at least one jam
            self.assertEqual(0, Jam.objects.filter(
                bout__isnull=True).count())

            


