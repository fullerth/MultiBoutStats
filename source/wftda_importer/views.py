from django.shortcuts import render

def view_stat_list(request):
    context = {'name':'Luna'}
    return render(request, 'wftda_importer/stat_display.html', context)
    
