from django.http import HttpResponse
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets

from .models import Tickets
from .serializers import TicketsSerializer
# from parkingrid.mysite.buy import serializers

# class TicketsViewSet(GenericViewSet,
#                  CreateModelMixin,
#                  RetrieveModelMixin,
#                  ListModelMixin):
#     serializer_class = TicketsSerializer
#     queryset = Tickets.objects.all()

class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all().order_by('license_plate')
    serializer_class = TicketsSerializer

# def index(request):
#     return HttpResponse("Hello, world. You're at the buying index.")

# def index(request):
