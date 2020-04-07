import datetime

from django.db import models
from django.utils import timezone


class NewsStory(models.Model):
    heading = models.CharField(max_length=200)
    pub_date = models.DateTimeField('published date')
    content = models.CharField(max_length=10000)

    def __str__(self):
        return self.heading

    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

