from django.db import models

# Create your models here.
class ShortenedUrl(models.Model):
    originalUrl = models.CharField(max_length=200)
    shortenedUrl = models.CharField(max_length=6, blank = True, null = True)
    createdTime = models.DateTimeField(auto_now_add=True) # won't be seen in admin as it's not editable
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        if self.title:
            return self.title
        return self.originalUrl
