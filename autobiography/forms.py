from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Autobiography

class AutobiographyForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Autobiography
        fields = ['title', 'content', 'file']

