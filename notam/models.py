from django.db import models

class Notam(models.Model):
    site_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'Site Name: {} Date: {}'.format(self.site_name, self.date)
        
    class Meta:
        managed = True
        db_table = 'notam'
