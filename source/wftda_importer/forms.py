from django import forms

class WftdaStatBookForm(forms.Form):
    stat_book = forms.FileField(label="Stat Book")
