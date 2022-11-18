import csv
import os

import django
from dotenv import load_dotenv

from weath.models import City

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fort.settings')
django.setup()


DATAFILE = os.getenv('DATAFILE')


def get_data_to_bd(filepath):
    with open(filepath, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data = City(
                name=row['name'],
                latitude=float(row['latitude']),
                longitude=float(row['longitude']),
                population=int(row['population'])
            )
            data.save()


if __name__ == '__main__':
    get_data_to_bd(DATAFILE)
