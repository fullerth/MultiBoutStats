from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return("{0}".format(self.name))

class Jam(models.Model):
    players = models.ManyToManyField(Player, through='PlayerToJam')

class PlayerToJam(models.Model):
    BLOCKER = 'B'
    JAMMER = 'J'
    PIVOT = 'P'
    POSITIONS = (
        (BLOCKER, 'Blocker'),
        (JAMMER, 'Jammer'),
        (PIVOT, 'Pivot'),
    )
    player = models.ForeignKey('Player', null=True)
    jam = models.ForeignKey('Jam', null=True)
    position = models.CharField(max_length=1, choices=POSITIONS, null=True)

class Bout(models.Model):
    location = models.CharField(max_length=200, null=True)
    home_roster = models.ForeignKey('Player', null=True)

    def __str__(self):
        return("{0}".format(self.home_roster.name))

class Roster(models.Model):
    players = models.ManyToManyField('Player')
