from django.db import models
from sitemaintenance.models import Sitemaintenance

class PointOfContact(models.Model):
    county_no = models.CharField(max_length=20, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    user_lvl = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    cell_or_alternate = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return 'County Number:  {} County: {} \
                Organization: {}  User Level: {}\
                Name: {}  phone: {}  job title: {}\
                Cell Phone or Alternate: {}\
                E-mail: {}\
                notes: {}'\
                .format(self.county_no, self.county,\
                        self.organization, self.user_lvl,\
                        self.name, self.phone, self.job_title,\
                        self.cell_or_alternate, self.email, \
                        self.notes )

    class Meta:
        managed = True
        db_table = 'contact'


class PointOfContactUpdate(models.Model):
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True)
    cell_or_alternate = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return 'County Number:  {} County: {} \
                Organization: {}  User Level: {}\
                Name: {}  phone: {}  job title: {}\
                Cell Phone or Alternate: {}\
                E-mail: {}\
                notes: {}'\
                .format(self.county, self.organization, \
                        self.name, self.phone, self.job_title,\
                        self.cell_or_alternate, self.email, \
                        self.notes )

    class Meta:
        managed = True
        db_table = 'update_contact'
