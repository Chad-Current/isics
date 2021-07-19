from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_delete
from django.dispatch import receiver
from pointofcontact.models import PointOfContactUpdate


class EmailTo(models.Model):
    name = models.CharField(max_length=255, null=True)
    county = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    is_active = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'email_list'

    def __str__(self):
        return f'{self.name}   {self.email}   {self.county}'
    
    @receiver(post_delete, sender=PointOfContactUpdate)
    def update_email_list(sender, instance, using, **kwargs):
        EmailTo.objects.create(name=instance.name, county=instance.county, email=instance.email, is_active=True)


class Sitemaintenance(models.Model):
    tower_cell = models.CharField(max_length=255)
    tower_assoc = ArrayField(models.CharField(max_length=2000))

    class Meta:
        managed = True
        db_table = 'sitemaintenance'

    def __str__(self):
        return f'{self.tower_cell}'

#class EmailSiteConnection
# EMAIL CLIENTS
class Email(models.Model):
    tower_cell = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
    sent_list = models.TextField(default='No record of email being sent')
    date = models.DateField(auto_now=False, auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'email_record'

    def __str__(self):
        return f'Subject:{self.subject}  Message:{self.message}  Date:{self.date}'
