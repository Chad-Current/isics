from django.db import models
from django.urls import reverse

class ServiceTicket(models.Model):
    ticketno = models.CharField(max_length=25) # MIGRATE TO MAKE UNIQUE
    site_loc = models.CharField(max_length=50)
    issue = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False, auto_now_add=False) #CHANGE FOR RUNTIME ERROR UTC TIME_ZONE ACTIVE??

    def get_absolute_url(self):
        return reverse('service-call-page')

    def __str__(self):
        return f'{self.ticketno}  {self.site_loc}   {self.issue}'

    class Meta:
        managed = True
        db_table = 'ticketlog'
