from django import forms
from .models import Video
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class VideoForm(forms.ModelForm):
    abstract = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Video
        fields = ['title', 'abstract', 'google_drive_link']
