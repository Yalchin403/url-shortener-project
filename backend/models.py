from django.db import models

# Create your models here.
class ShortenedUrl(models.Model):
    originalUrl = models.CharField(max_length=200)
    shortenedUrl = models.CharField(max_length=6, blank = True, null = True)
    createdTime = models.DateTimeField(auto_now_add=True) # won't be seen in admin as it's not editable
    
    def __str__(self):
        return self.originalUrl
