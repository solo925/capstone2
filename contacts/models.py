from django.db import models

class Contact(models.Model):
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    discord = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "Contact Information"

