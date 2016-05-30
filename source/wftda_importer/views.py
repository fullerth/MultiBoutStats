from django.shortcuts import render

def view_stat_list(request, player_id=1):
    context = {'name':'Luna'}
    return render(request, 'wftda_importer/stat_display.html', context)
    
