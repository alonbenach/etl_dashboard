from django.urls import path
from .views import (
    EventListCreateView,
    DailyMetricListView,
    metrics_dashboard,
)

urlpatterns = [
    path("events/", EventListCreateView.as_view(), name="event-list-create"),
    path("metrics/", DailyMetricListView.as_view(), name="daily-metric-list"),
    path("dashboard/metrics/", metrics_dashboard, name="metrics_dashboard"),
]
