from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class PointOfContactUpdate(models.Model):
    name = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True)
    cell_or_alternate = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('pointofcontact:point-of-contact-page')

    def __str__(self):
        return f'Name: {self.name}'

    class Meta:
        managed = True
        db_table = 'update_contact'



class PointOfContact(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    cell_or_alternate = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse('point-of-contact-page')

    def __str__(self):
        return f'Name: {self.name}'

    @receiver(pre_delete, sender=PointOfContactUpdate)
    def update_delete(sender, instance, using, **kwargs):
        PointOfContact.objects.create(id=instance.id, name=instance.name, county=instance.county, \
                                      organization=instance.organization, phone=instance.phone, \
                                      job_title=instance.job_title, cell_or_alternate=instance.cell_or_alternate, \
                                      email=instance.email, notes=instance.notes)

    class Meta:
        managed = True
        db_table = 'contact'
