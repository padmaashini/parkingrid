# Generated by Django 4.0.3 on 2022-04-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_issued', models.DateField()),
                ('license_plate', models.CharField(max_length=10)),
                ('duration', models.IntegerField(choices=[(30, '30 minutes'), (60, '1 hour'), (120, '2 hours')])),
            ],
        ),
    ]
