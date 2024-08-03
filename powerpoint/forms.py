from django import forms
from .models import PowerPoint

class PowerPointForm(forms.ModelForm):
    class Meta:
        model = PowerPoint
        fields = ['title', 'file']
