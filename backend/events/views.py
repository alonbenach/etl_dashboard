from rest_framework import generics
from .models import Event, DailyMetric
from .serializers import EventSerializer, DailyMetricSerializer


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class DailyMetricListView(generics.ListAPIView):
    queryset = DailyMetric.objects.all()
    serializer_class = DailyMetricSerializer
