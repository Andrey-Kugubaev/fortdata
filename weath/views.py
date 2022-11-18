import logging
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fort.settings')

import time
import django

django.setup()

import requests
import schedule
from dotenv import load_dotenv

import models
import script_by_bd

load_dotenv()

appid = os.getenv('APPID')
DATAFILE = os.getenv('DATAFILE')

logging.basicConfig(
    level=logging.INFO,
    filename='main.log',
    format='%(asctime)s, %(levelname)s, %(name)s, %(message)s'
)

logging.basicConfig(level=logging.INFO)


def get_weather_info():
    cities = models.City.objects.all()
    for city in cities:
        latitude = city.latitude
        longitude = city.longitude
        city_id = models.City.objects.get(name=city)
        try:
            info_result = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}'
                f'&lon={longitude}&appid={appid}&units=metric'
            )
            weather_info = info_result.json()
            models.Weather.objects.create(
                temp=weather_info['main']['temp'],
                feels=weather_info['main']['feels_like'],
                humidity=weather_info['main']['humidity'],
                city=city_id
            )
        except Exception as error:
            logging.error(f'Ошибка при запросе к основному API: {error}')
            models.Weather.objects.create(
                temp=100,
                feels=100,
                humidity=-1,
                city=city_id
            )


def scheduler():
    schedule.every().hour.do(get_weather_info)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    script_by_bd.get_data_to_bd(DATAFILE)
    get_weather_info()
    scheduler()
