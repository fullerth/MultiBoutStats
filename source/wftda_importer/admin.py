from django.contrib import admin

from wftda_importer.models import Player, Jam, PlayerToJam

# Register your models here.
admin.site.register(Player)
admin.site.register(Jam)
admin.site.register(PlayerToJam)

