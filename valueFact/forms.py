from django import forms
from .models import ValueFactPost

class ValueFactForm(forms.ModelForm):

    class Meta:
        model=ValueFactPost
        fields=('title','text',)