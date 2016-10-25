from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def view_wftda_importer(request):
    return(render(request, 'wftda_importer/import.html'))
