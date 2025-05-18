from django.db import models


class Event(models.Model):
    user_id = models.CharField(max_length=50)
    session_id = models.CharField(max_length=100)
    event_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField()


class DailyMetric(models.Model):
    date = models.DateField(unique=True)
    dau = models.IntegerField()
    avg_events_per_user = models.FloatField()
