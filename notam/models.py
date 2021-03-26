from django.db import models
from user.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.urls import reverse


class Notam(models.Model):
    site_name = models.CharField(max_length=255)
    user =  models.ForeignKey(User, on_delete=models.DO_NOTHING)
    aviation = models.CharField(max_length=255)
    motorola = models.CharField(max_length=255)
    notes = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'Site Name: {} Date: {}'.format(self.site_name, self.date)

    def get_absolute_url(self):
        return reverse('notam:notam-all')
    
    class Meta:
        managed = True
        db_table = 'notam'

class NotamExtend(models.Model):
    reason = models.CharField(max_length=1000)
    original_notam = models.ForeignKey(Notam, on_delete=models.CASCADE)
    user_ex = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'User: {self.user}  reason: {self.reason}'

    def get_absolute_url(self):
        return reverse('notam:notam-all')

    class Meta:
        managed = True
        db_table = 'notam_extend'

class NotamArchive(models.Model):
    site_name = models.CharField(max_length=255)
    user =  models.ForeignKey(User, on_delete=models.DO_NOTHING)
    aviation = models.CharField(max_length=255)
    motorola = models.CharField(max_length=255)
    notes = models.CharField(max_length=1000)
    extends = models.CharField(max_length=5000)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return 'Site Name: {} Date: {}'.format(self.site_name, self.date)

    def get_absolute_url(self):
        return reverse('notam:notam-all')

    @receiver(pre_delete, sender=Notam)
    def notam_archive(sender, instance, using, **kwargs):
        extends = NotamExtend.objects.filter(original_notam_id=instance.id).last()
        extends = extends.reason
        NotamArchive.objects.create(site_name=instance.site_name, aviation=instance.aviation, \
                                    motorola=instance.motorola, notes=instance.notes, extends=extends, date=instance.date, \
                                    user_id=instance.user_id)


    class Meta:
        managed = True
        db_table = 'notam_archive'
