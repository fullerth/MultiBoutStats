import factory

from . import models

class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Player

    name = "Cassie Beck"
