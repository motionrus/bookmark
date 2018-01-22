from django.db import models
from django.contrib.auth.models import User


class BookMark(models.Model):
    pub_date = models.DateTimeField('date saved')
    url = models.URLField(max_length=200)
    site_name = models.TextField(max_length=200, default='')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, default='None')
    image = models.URLField(max_length=200, default='')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=True, blank=True)

    def __str__(self):
        return self.title


class Word_Analytics(models.Model):
    word = models.CharField(max_length=255, default='')
    bookmark = models.ForeignKey(
        BookMark, on_delete=models.CASCADE,
        null=False, blank=False)
    frequency = models.IntegerField(default=0)

    def __str__(self):
        return str(self.bookmark) + "||" + str(self.word) + "||" + str(self.frequency)
