from django.db import models

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to='profile_photo/',null=True,blank=True)
    
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ""
    #     return url
    
    