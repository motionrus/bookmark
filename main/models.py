
import datetime
from django.db import models
from django.utils import timezone


class BookMark(models.Model):
    pub_date = models.DateTimeField('date saved')
    url = models.URLField(max_length=200)
    site_name = models.TextField(max_length=200, default='')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, default='None')
    image = models.URLField(max_length=200, default='')

    def __str__(self):
        return self.title
