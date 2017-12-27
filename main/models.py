
import datetime
from django.db import models
from django.utils import timezone


class BookMark(models.Model):
    pub_date = models.DateTimeField('date saved')
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=255)
    text = models.TextField()
    short_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title
