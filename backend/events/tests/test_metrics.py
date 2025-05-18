from django.test import TestCase
from django.utils import timezone
from events.models import Event, DailyMetric
from datetime import timedelta, date


class MetricsCalculationTest(TestCase):
    def setUp(self):
        today = timezone.now().date()
        # yesterday = used by DAG
        self.yesterday = today - timedelta(days=1)

        # Create 3 events for user 1 and 2 events for user 2 (yesterday)
        Event.objects.create(
            user_id=1,
            timestamp=timezone.make_aware(
                timezone.datetime.combine(self.yesterday, timezone.datetime.min.time())
            ),
        )
        Event.objects.create(
            user_id=1,
            timestamp=timezone.make_aware(
                timezone.datetime.combine(self.yesterday, timezone.datetime.min.time())
            ),
        )
        Event.objects.create(
            user_id=1,
            timestamp=timezone.make_aware(
                timezone.datetime.combine(self.yesterday, timezone.datetime.min.time())
            ),
        )
        Event.objects.create(
            user_id=2,
            timestamp=timezone.make_aware(
                timezone.datetime.combine(self.yesterday, timezone.datetime.min.time())
            ),
        )
        Event.objects.create(
            user_id=2,
            timestamp=timezone.make_aware(
                timezone.datetime.combine(self.yesterday, timezone.datetime.min.time())
            ),
        )

    def test_event_model_counts(self):
        self.assertEqual(Event.objects.count(), 5)

    def test_dailymetric_insert_logic(self):
        # Simulate the same query logic from your DAG
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO events_dailymetric (date, dau, avg_events_per_user)
                SELECT
                    DATE(timestamp) AS date,
                    COUNT(DISTINCT user_id),
                    COUNT(*) * 1.0 / COUNT(DISTINCT user_id)
                FROM events_event
                WHERE DATE(timestamp) = %s
                GROUP BY DATE(timestamp)
                ON CONFLICT (date) DO NOTHING;
            """,
                [self.yesterday],
            )

        metrics = DailyMetric.objects.get(date=self.yesterday)
        self.assertEqual(metrics.dau, 2)
        self.assertAlmostEqual(metrics.avg_events_per_user, 2.5, places=1)
