import factory

from . import models

class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Player

    name = factory.Sequence(lambda n: "player{0}".format(n))

class JamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Jam

class JamWithPlayersFactory(JamFactory):
    players = factory.RelatedFactory(PlayerFactory)

class PlayerToJamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.PlayerToJam

    player = factory.SubFactory(PlayerFactory)
    jam = factory.SubFactory(JamFactory)
    position = factory.Iterator([models.PlayerToJam.BLOCKER, 
        models.PlayerToJam.PIVOT, models.PlayerToJam.JAMMER])

class RosterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Roster

class RosterWithPlayersFactory(RosterFactory):
    """Creates and adds four players to a new Roster"""
    @factory.post_generation
    def players(self, create, extracted, **kwargs):
        if extracted:
            for player in extracted:
                self.players.add(player)
        else:
            self.players.add(PlayerFactory())
            self.players.add(PlayerFactory())
            self.players.add(PlayerFactory())
            self.players.add(PlayerFactory())

class BoutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Bout

    location = factory.Sequence(lambda n: "Location{0}".format(n))
    home_roster = factory.SubFactory(RosterFactory)

class CompleteBoutFactory(BoutFactory):
    home_roster = factory.SubFactory(RosterWithPlayersFactory)

    jam = factory.RelatedFactory(JamFactory, 'bout')

