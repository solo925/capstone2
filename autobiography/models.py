from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Autobiography(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='autobiography/', null=True, blank=True)

    def __str__(self):
        return self.title





