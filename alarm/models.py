from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Alarm(models.Model):
    site_name = models.CharField(max_length=50)
    site_identity = models.CharField(max_length=50)
    alarm = models.CharField(max_length=2000)
    alarm_date = models.CharField(max_length=255) #Check Record for formatting details
    ticket_closed = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(auto_now=False, auto_now_add=False) # Change to auto_now_add = True
    ### Awaiting to see how Zapier logs emails into Postgresql first before commit##
    ################################################################################
    # rcvd_email = models.ForeignKey(AlarmEmail, on_delete=models.cascade)
    ################################################################################
    def get_absolute_url(self):
        return reverse('alarm-check:alarm-home')

    def __str__(self):
        return f'Site Indentity {self.site_identity}  Alarm Date: {self.alarm_date}'

    class Meta:
        managed = True
        db_table = 'alarm'

class AlarmComment(models.Model):
    time_stamp = models.DateTimeField(auto_now=False, auto_now_add=False) # Change to auto_now = True
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
    arcv_site_name = models.CharField(max_length=50)
    arcv_site_identity = models.CharField(max_length=50) #Neccassary?
    arcv_alarm = models.CharField(max_length=2000)
    arcv_alarm_date = models.CharField(max_length=255)
    # arcv_dispatch = models.BooleanField(default=False) #Neccassary?
    # arcv_dispatch_personnel = models.CharField(max_length=50, blank=True)
    # arcv_dipatch_date = models.DateTimeField(auto_now=False, auto_now_add=False) #SPELLING ERROR
    arcv_ticket_closed = models.BooleanField(default=False)
    all_comments = models.CharField(max_length=2000)
    time_stamp = models.DateTimeField(auto_now=False, auto_now_add=False)

    def get_absolute_url(self):
        return reverse('alarm-check:alarm-list')

    def __str__(self):
        return f'ARC Site Indentity {self.arcv_site_identity}  ARC Alarm Date: {self.arcv_alarm_date}'



    class Meta:
        managed = True
        db_table = 'alarm_archive'



### Awaiting to see how Zapier logs emails into Postgresql first before commit##
################################################################################
# class AlarmEmail(models.Model):
#     email_subject = models.CharField(max_length=255) # Alarm type
#     email_body = models.CharField(max_length=2000) # Extras
#
#     class Meta:
#         managed = True
#         db_table = 'alarm_email'
#
#     def __str__(self):
#         return f'{self.email_subject}  :   {self.email_body}'
###############################################################################
