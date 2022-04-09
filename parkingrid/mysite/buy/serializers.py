# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Tickets

class TicketsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tickets
        fields = (
            'id', 'time_issued', 'license_plate', 'duration'
        )