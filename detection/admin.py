from django.contrib import admin
from .models import FireSmokeAlert

@admin.register(FireSmokeAlert)
class FireSmokeAlertAdmin(admin.ModelAdmin):
    list_display = ('id', 'alert_type', 'detected_at')
    search_fields = ('alert_type',)
