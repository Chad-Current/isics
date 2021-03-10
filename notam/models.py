from django.db import models
from user.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver

class Notam(models.Model):
    site_name = models.CharField(max_length=255)
    user =  models.ForeignKey(User, on_delete=models.DO_NOTHING)
    aviation = models.CharField(max_length=255)
    motorola = models.CharField(max_length=255)
    notes = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'Site Name: {} Date: {}'.format(self.site_name, self.date)

    class Meta:
        managed = True
        db_table = 'notam'

class NotamArchive(models.Model):
    site_name = models.CharField(max_length=255)
    user =  models.ForeignKey(User, on_delete=models.DO_NOTHING)
    aviation = models.CharField(max_length=255)
    motorola = models.CharField(max_length=255)
    notes = models.CharField(max_length=1000)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return 'Site Name: {} Date: {}'.format(self.site_name, self.date)

    @receiver(pre_delete, sender=Notam)
    def notam_archive(sender, instance, using, **kwargs):
        NotamArchive.objects.create(id=instance.id, site_name=instance.site_name, user=instance.user, aviation=instance.aviation, \
                                    motorola=instance.motorola, notes=instance.notes, date=instance.date)


    class Meta:
        managed = True
        db_table = 'notam_archive'
