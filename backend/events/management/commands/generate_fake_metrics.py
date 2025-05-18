from django.core.management.base import BaseCommand
from events.models import Event
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = "Generate fake Event data for the last 30 days"

    def handle(self, *args, **kwargs):
        Event.objects.all().delete()
        base = datetime.now()

        user_ids = [f"user_{i}" for i in range(1, 11)]  # 10 fake users

        for day in range(30):
            date = base - timedelta(days=day)
            for _ in range(random.randint(5, 20)):  # 5–20 events per day
                Event.objects.create(
                    timestamp=date.replace(
                        hour=random.randint(0, 23), minute=random.randint(0, 59)
                    ),
                    user_id=random.choice(user_ids),
                    event_type=random.choice(["login", "view", "click", "purchase"]),
                )

        self.stdout.write(self.style.SUCCESS("✅ 30 days of fake events generated."))
