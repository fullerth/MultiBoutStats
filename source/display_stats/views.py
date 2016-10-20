from django.shortcuts import render, get_object_or_404

from wftda_importer.models import Player, Jam, PlayerToJam, Bout

def view_stat_list(request, player_id=1):
    p = get_object_or_404(Player, pk=player_id)
    list_of_bouts = Bout.objects.filter(home_roster__players=p)
    bouts_played = list_of_bouts.count()
    num_jams = Jam.objects.filter(players=p).count()
    total_jams_available = Jam.objects.filter(
            bout__id__in=list_of_bouts).count()
    blocker_jams = PlayerToJam.objects.filter(player=p).filter(
            position=PlayerToJam.BLOCKER).count()
    jammer_jams = PlayerToJam.objects.filter(player=p).filter(
            position=PlayerToJam.JAMMER).count()
    pivot_jams = PlayerToJam.objects.filter(player=p).filter(
            position=PlayerToJam.PIVOT).count()
    lead_jams = PlayerToJam.objects.filter(player=p, lead_flag=True).count()
    context = {'name':p.name, 'bouts_played':bouts_played, 'num_jams':num_jams,
               'total_jams_available':total_jams_available, 
               'blocker_jams':blocker_jams, 'jammer_jams':jammer_jams, 
               'pivot_jams':pivot_jams, 'lead_jams': lead_jams,
              }
    return render(request, 'display_stats/display_stats.html', context)

    
