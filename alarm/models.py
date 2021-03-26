from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.urls import reverse
import re

class Alarm(models.Model):
    site = models.CharField(max_length=1000)
    alarm = models.CharField(max_length=1000)
    opened  = models.CharField(max_length=1000)
    ticket = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    notes = models.CharField(max_length=1000)
    email = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now=False, auto_now_add=True, blank=True)

    def __init__(self, site, alarm, opened, ticket, priority, status, notes, email, timestamp, *args, **kwargs):
        super().__init__(site, alarm, opened, ticket, priority, status, notes, email, timestamp, *args, **kwargs)
        Ticket = '(?<=Ticket)\s\w+'
        Notes = 'Notes:(.*)|Status:(.*)|Communications:(.*)|Assigned To:(.*)'
        Priority = 'High'
        Status = '(?<=High - )\w+'
        Opened = '(?<=Opened:)\s+(.*)(?=\(\(GMT)'
        Site = '(^[A-Z]\w+\s[A-Z][a-z]\w+)|(^[A-Z]\d+\s[A-Z][a-z]\w+)|(^[A-Z]\w+)'
        Alarm = '((?<=DI:)\w+|NOT WIDE TRUNKING SITE)'
        Email = '(.*)'

        if 'Ticket' in self.ticket:
            #Ticket
            self.ticket = re.search(f'{Ticket}',self.ticket)
            if self.ticket:
                self.ticket = self.ticket.group()
            else:
                self.ticket = 'Data missing'
            #Notes
            self.notes = re.search(f'{Notes}',self.notes)
            if self.notes:
                self.notes = self.notes.group()
            else:
                self.notes = 'Data missing'
            #Priority
            self.priority = re.search(f'{Priority}',self.priority)
            if self.priority:
                self.priority = self.priority.group()
            else:
                self.priority = 'Data missing'
            #Status
            self.status = re.search(f'{Status}',self.status)
            if self.status:
                self.status = self.status.group()
            else:
                self.status = 'Data missing'
            #Opened
            self.opened = re.search(f'{Opened}',self.opened)
            if self.opened:
                self.opened = self.opened.group()
            else:
                self.opened = 'Data missing'
            #Site
            self.site = re.search(f'{Site}',self.site)
            if self.site:
                self.site = self.site.group()
            else:
                self.site = 'Data missing'
            #Alarms
            self.alarm = re.search(f'{Alarm}',self.alarm)
            if self.alarm:
                self.alarm = self.alarm.group()
            else:
                self.alarm = 'Data missing'
            #Email
            self.email = re.search(f'{Email}',self.email)
            if self.email:
                self.email = self.email.group()
            else:
                self.email = 'Data missing'



    def get_absolute_url(self):
        return reverse('alarm-check:alarm-home')

    def __str__(self):
        return f'Site Indentity {self.site}  Alarm Date: {self.timestamp}'

    class Meta:
        managed = True
        db_table = 'alarm'

class AlarmComment(models.Model):
    time_stamp = models.DateTimeField(auto_now=False, auto_now_add=True) # Change to auto_now = True
    comments = models.CharField(max_length=250)
    original_alarm = models.ForeignKey(Alarm, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('alarm-check:alarm-home')

    def __str__(self):
        return f'Comments: {self.comments}  Time: {self.time_stamp}'

    class Meta:
        managed = True
        db_table = 'alarmtrace'


class AlarmArchive(models.Model):
    arcv_site_name = models.CharField(max_length=5000)
    arcv_alarm = models.CharField(max_length=5000)
    arcv_alarm_opened = models.CharField(max_length=5000)
    arcv_ticket = models.CharField(max_length=255)
    all_comments = models.CharField(max_length=5000)
    time_stamp = models.DateField(auto_now=False, auto_now_add=True, blank=True)

#    @receiver(post_delete, sender=Alarm)
#    def del_alarm(self, instance, *args, **kwargs):
#        try:
#            Alarm.objects.filter(ticket__iexact=instance.arcv_ticket).delete()
#        except IntergrityError as e:
#            print('Could not find objects')


    def get_absolute_url(self):
        return reverse('alarm-check:alarm-list')

    def __str__(self):
        return f'ARC Site Name {self.arcv_site_name}  ARC Alarm Date: {self.arcv_alarm_opened}'

    

    class Meta:
        managed = True
        db_table = 'alarm_archive'



