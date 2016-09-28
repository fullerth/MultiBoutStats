from django.shortcuts import render, get_object_or_404

from wftda_importer.models import Player, Jam, PlayerToJam, Bout

def view_stat_list(request, player_id=1):
    p = get_object_or_404(Player, pk=player_id)
    bouts_played = Bout.objects.filter(home_roster__players=p).count()
    num_jams = Jam.objects.filter(players=p).count()
    total_jams = Jam.objects.all().count()
    blocker_jams = PlayerToJam.objects.filter(player=p).filter(
            position=PlayerToJam.BLOCKER).count()
    jammer_jams = PlayerToJam.objects.filter(player=p).filter(
            position=PlayerToJam.JAMMER).count()
    pivot_jams = PlayerToJam.objects.filter(player=p).filter(
            position=PlayerToJam.PIVOT).count()
    context = {'name':p.name, 'bouts_played':bouts_played, 'num_jams':num_jams,
               'total_jams':total_jams, 'blocker_jams':blocker_jams, 
               'jammer_jams':jammer_jams, 'pivot_jams':pivot_jams
              }
    return render(request, 'display_stats/display_stats.html', context)

    
