from rest_framework import generics
from .models import Event, DailyMetric
from .serializers import EventSerializer, DailyMetricSerializer
from django.shortcuts import render


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class DailyMetricListView(generics.ListAPIView):
    queryset = DailyMetric.objects.all()
    serializer_class = DailyMetricSerializer


def metrics_dashboard(request):
    metrics = DailyMetric.objects.order_by("-date")[:30]
    return render(request, "events/dashboard.html", {"metrics": metrics})
