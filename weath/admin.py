from django.contrib import admin

from weath.models import City, Weather


class CityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'latitude', 'longitude', 'population',)
    list_filter = ('name',)


class WeatherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'temp', 'feels', 'humidity', 'time', 'city',)
    list_filter = ('city',)


admin.site.register(City, CityAdmin)
admin.site.register(Weather, WeatherAdmin)
