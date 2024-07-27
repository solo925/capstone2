from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    abstract = models.TextField()
    google_drive_link = models.URLField(null=True,blank=True)  # Store the Google Drive video URL
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_drive_embed_url(self):
        # Extract the file ID from the Google Drive URL
        file_id = self.google_drive_link.split('/')[-2]
        return f"https://drive.google.com/file/d/{file_id}/preview"
