from django.urls import reverse
from django.test import TestCase
from events.models import DailyMetric


class MetricsViewTests(TestCase):
    def setUp(self):
        DailyMetric.objects.create(
            date="2024-05-01",
            dau=10,
            avg_events_per_user=2.5,
        )

    def test_metrics_api(self):
        response = self.client.get(reverse("daily-metric-list"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("application/json", response["Content-Type"])

    def test_dashboard_view(self):
        response = self.client.get(reverse("metrics_dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Daily Metrics")
        self.assertContains(response, "DAU")
