from django.db import models
from django.contrib.auth.models import User


class ShortenedUrl(models.Model):
    originalUrl = models.TextField()
    shortenedUrl = models.CharField(max_length=6, blank = True, null = True)
    createdTime = models.DateTimeField(auto_now_add=True) # won't be seen in admin as it's not editable
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        if self.owner:
            return self.title + ' - ' +self.owner.username
        return self.originalUrl
