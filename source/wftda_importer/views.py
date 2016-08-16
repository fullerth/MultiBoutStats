from django.shortcuts import render, get_object_or_404

def view_wftda_importer(request):
    return(render(request, 'wftda_importer/import.html'))
