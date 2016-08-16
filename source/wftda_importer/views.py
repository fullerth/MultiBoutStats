from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django import forms

class WftdaImporterForm(forms.Form):
    file_input = forms.FileField()

def view_wftda_importer(request):
    if request.method == 'POST':
        form = WftdaImporterForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect('/display_stats')
    else:
        form = WftdaImporterForm()

    context = {'form':form}
    return(render(request, 'wftda_importer/import.html', context))

