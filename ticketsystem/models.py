from django.db import models
from django.urls import reverse

class SubscriberTicket(models.Model):
    badge_identifier = models.CharField(max_length=25)
    location = models.CharField(max_length=255)
    talkgroup_assoc = models.CharField(max_length=255)
    rssi = models.IntegerField(default=0)
    mobile = models.BooleanField(default=False)
    portable = models.BooleanField(default=False)
    desc_issue = models.CharField(max_length=1500)
    issue_resolved = models.BooleanField(blank=True)
    desc_resolve = models.CharField(max_length=1500, blank=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('ticketsystem:ticket-system-page')

    def __str__(self):
        return f'{self.badge_identifier}{self.talkgroup_assoc}{self.talkgroup_assoc}'

    class Meta:
        managed = True
        db_table = 'subscriber_tickets'
