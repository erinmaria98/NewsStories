import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Headline(models.Model):
    headline_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.headline_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Story(models.Model):
    headline = models.ForeignKey(Headline, on_delete=models.CASCADE)
    story_text = models.CharField(max_length=1000)
    def __str__(self):
        return self.story_text
    
