from django.db import models

# Create your models here.
class Tickets(models.Model):
    DURATIONS = [
        (30, '30 minutes'), 
        (60, '1 hour'), 
        (120, '2 hours')
    ]
    time_issued = models.DateField()
    license_plate = models.CharField(max_length=10)
    duration = models.IntegerField(choices = DURATIONS)

    def __str__(self):
        return self.license_plate