from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return("{0}".format(self.name))

class Jam(models.Model):
    players = models.ManyToManyField(Player)

