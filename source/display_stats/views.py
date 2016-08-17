from django.shortcuts import render, get_object_or_404

from wftda_importer.models import Player, Jam

def view_stat_list(request, player_id=1):
    p = get_object_or_404(Player, pk=player_id)
    num_jams = Jam.objects.filter(players=p).count()
    total_jams = Jam.objects.all().count()
    context = {'name':p.name, 'num_jams': num_jams, 'total_jams': total_jams}
    return render(request, 'display_stats/display_stats.html', context)
    
