## 📊 Demo Data

This project uses generated test data to populate event metrics.

To load fake data for the dashboard:

```bash
docker-compose exec web python manage.py generate_fake_metrics
```
This simulates 30 days of activity (DAU, avg events/user) for visualizing the chart and API output.