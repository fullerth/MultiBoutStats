from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return("{0}".format(self.name))

class Jam(models.Model):
    players = models.ManyToManyField(Player, through='PlayerToJam')

class PlayerToJam(models.Model):
    player = models.ForeignKey('Player', null=True)
    jam = models.ForeignKey('Jam', null=True)
