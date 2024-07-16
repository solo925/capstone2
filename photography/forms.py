from django import forms
from .models import PhotoEssay

class PhotoEssayForm(forms.ModelForm):
    class Meta:
        model = PhotoEssay
        fields = ['title', 'content', 'file']
