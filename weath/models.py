from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    population = models.IntegerField()

    def __str__(self):
        return self.name


class Weather(models.Model):
    temp = models.DecimalField(max_digits=6, decimal_places=2)
    feels = models.DecimalField(max_digits=6, decimal_places=2)
    humidity = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
