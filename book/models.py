from django.db import models

# Create your models here.


class Translate(models.Model):
    english_text = models.TextField()
    russian_text = models.TextField()

    def __str__(self):
        return 'EN "{}", RU "{}"'.format(self.english_text[:10], self.russian_text[:10])