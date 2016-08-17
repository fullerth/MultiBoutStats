from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import FormView

from django import forms

class WftdaImporterForm(forms.Form):
    file_input = forms.FileField()

class WftdaImporterFormView(FormView):
    template_name = 'wftda_importer/import.html'
    form_class = WftdaImporterForm
    success_url = '/display_stats'

    def form_valid(self, form):
        print("VALID FORM DATA, now do something with it")
        return super(WftdaImporterFormView, self).form_valid(form)


