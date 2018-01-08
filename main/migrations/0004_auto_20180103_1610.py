# Generated by Django 2.0 on 2018-01-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171215_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='short_text',
        ),
        migrations.RemoveField(
            model_name='bookmark',
            name='text',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='description',
            field=models.TextField(default='None', max_length=500),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='image',
            field=models.URLField(default=''),
        ),
    ]