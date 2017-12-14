
import datetime
from django.db import models
from django.utils import timezone

class BookMarks(models.Model):
    pub_date = models.DateTimeField('date saved')
    url = models.URLField(max_length=200)
    url_title = models.CharField(max_length=255)
    url_text = models.TextField()
    url_preview = models.CharField(max_length=255)

