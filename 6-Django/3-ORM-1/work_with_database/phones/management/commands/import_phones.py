import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            pm = Phone(
                    id = int(phone['id']),
                    name = phone['name'],
                    image = phone['image'],
                    price = float(phone['price']),
                    release_date = phone['release_date'],
                    lte_exists = bool(phone['lte_exists']),
                    slug = slugify(phone['name']))
            pm.save()



