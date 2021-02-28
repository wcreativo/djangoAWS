from django.db import models
from django.shortcuts import redirect

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField()
    bucket = models.CharField(max_length=100, null=False, blank=False)
    key_path = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '{}'.format(redirect('albums:list').url)
