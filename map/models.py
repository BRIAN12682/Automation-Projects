from django.db import models

class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    latitude = models.FloatField(null=True, blank=True, editable=False)
    longitude = models.FloatField(null=True, blank=True, editable=False)
    country = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address




from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone
from django.utils import timezone
# models.py
from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=100)
    contact = models.CharField(max_length=25)
    address = models.CharField(max_length=200, null=True)
    remaining_days = models.IntegerField(blank=True, null=True, editable=False)
    link = models.URLField("Google Form Link", null=True, blank=True)  # Auto-calculated field

    def save(self, *args, **kwargs):
        # Calculate remaining days including the time before saving
        event_datetime = timezone.make_aware(timezone.datetime.combine(self.date, self.time))
        remaining_time = event_datetime - timezone.now()
        self.remaining_days = max(remaining_time.days, 0)  # Ensure remaining_days is non-negative
        super().save(*args, **kwargs)

    @property
    def datetime(self):
        return timezone.make_aware(timezone.datetime.combine(self.date, self.time))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Event Detail'
        verbose_name_plural = 'Event Details'
