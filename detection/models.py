from django.db import models

class FireSmokeAlert(models.Model):
    alert_type = models.CharField(max_length=100)  # Fire or Smoke
    image = models.ImageField(upload_to='alerts/')  # Upload location
    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alert_type} - {self.detected_at}"
