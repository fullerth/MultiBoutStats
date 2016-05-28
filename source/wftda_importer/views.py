from django.shortcuts import render

def view_stat_list(request):
    context = {}
    return render(request, 'wftda_importer/stat_display.html', context)
    
