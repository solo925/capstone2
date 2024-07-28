from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Video(models.Model):
    title = models.CharField(max_length=100)
    abstract = RichTextUploadingField(null=True, blank=True)  # Use CKEditor for abstract
    google_drive_link = models.URLField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_drive_embed_url(self):
        file_id = self.google_drive_link.split('/')[-2]
        return f"https://drive.google.com/file/d/{file_id}/preview"
