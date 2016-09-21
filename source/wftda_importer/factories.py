import factory

from . import models

class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Player

    name = factory.Sequence(lambda n: "player{0}".format(n))

class JamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Jam


class PlayerToJamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.PlayerToJam

    player = factory.SubFactory(PlayerFactory)
    jam = factory.SubFactory(JamFactory)
    position = factory.Iterator([models.PlayerToJam.BLOCKER, 
        models.PlayerToJam.PIVOT, models.PlayerToJam.JAMMER])

class BoutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Bout

    location = factory.Sequence(lambda n: "Location{0}".format(n))
    home_roster = factory.SubFactory(PlayerFactory)

