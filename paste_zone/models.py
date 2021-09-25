from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class PasteZone(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    slug = models.CharField(max_length=6, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createdTime = models.DateTimeField(auto_now_add=True) # won't be seen in admin as it's not editable
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
         return self.title
