from django.db import models

# Create your models here.
class ShortenedUrl(models.Model):
    originalUrl = models.CharField(max_length=200)
    shortenedUrl = models.CharField(max_length=6, blank = True, null = True)
    createdTime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.originalUrl