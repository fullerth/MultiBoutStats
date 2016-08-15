from django.shortcuts import render, get_object_or_404

from wftda_importer.models import Player

def view_stat_list(request, player_id=1):
    p = get_object_or_404(Player, pk=player_id)
    context = {'name':p.name}
    return render(request, 'display_stats/display_stats.html', context)
    
