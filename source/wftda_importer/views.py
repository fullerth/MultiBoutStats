from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import WftdaStatBookForm

@login_required
def view_wftda_importer(request):
    context = {'form':WftdaStatBookForm()}
    return render(request, 'wftda_importer/import.html', context)
