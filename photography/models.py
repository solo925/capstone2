from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class PhotoEssay(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(null=True,blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='photo_essays/', null=True, blank=True)

    def __str__(self):
        return self.title

