from django.urls import path
from .views import EventListCreateView, DailyMetricListView

urlpatterns = [
    path("events/", EventListCreateView.as_view(), name="event-list-create"),
    path("metrics/", DailyMetricListView.as_view(), name="daily-metric-list"),
]
