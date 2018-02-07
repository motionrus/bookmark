from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from book.models import English
import os

FILE = r'extra\Ya---legenda.html'



def parse():
    with open(FILE, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    final_list = list()
    for tag in soup.findAll('tr'):
        [x.extract() for x in tag.a]
        english, russian = [x.get_text() for x in tag.findAll('td')]
        english = english.replace('\n', ' ').strip().replace('_', '').replace('  ', ' ')
        russian = russian.replace('\n', ' ').strip().replace('_', '').replace('  ', ' ')
        final_list.append([english, russian])
    for final in final_list:
        model = English()
        model.english_text = final[0]
        model.russian_text = final[1]
        model.save()


class Command(BaseCommand):
    help = 'You need put html file in root dir'

    def handle(self, *args, **options):
        parse()
        self.stdout.write('success')
