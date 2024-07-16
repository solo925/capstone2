from django.db import models

class CV(models.Model):
    LANGUAGE_CHOICES = (
        ('english', 'English'),
        ('kiswahili', 'Kiswahili'),
        ('indigenous', 'Indigenous'),
    )
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    file = models.FileField(upload_to='cv/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_language_display()} CV"
