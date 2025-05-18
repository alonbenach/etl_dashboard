from django.core.management.base import BaseCommand
from events.models import DailyMetric
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = "Generate fake DailyMetric data for testing"

    def handle(self, *args, **kwargs):
        base = date.today()
        DailyMetric.objects.all().delete()
        for i in range(30):
            d = base - timedelta(days=i)
            dau = random.randint(5, 50)
            avg = round(random.uniform(1.5, 4.5), 2)
            DailyMetric.objects.create(date=d, dau=dau, avg_events_per_user=avg)
        self.stdout.write(self.style.SUCCESS("✅ Fake metrics generated"))
