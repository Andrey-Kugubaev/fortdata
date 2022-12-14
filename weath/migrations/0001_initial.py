# Generated by Django 4.1.3 on 2022-11-17 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=8)),
                ('population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.DecimalField(decimal_places=2, max_digits=6)),
                ('feels', models.DecimalField(decimal_places=2, max_digits=6)),
                ('humidity', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weath.city')),
            ],
        ),
    ]
