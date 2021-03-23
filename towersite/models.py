from django.db import models

class Site(models.Model):
    site_name = models.CharField(max_length=255, default='Unknown')
    site_id = models.IntegerField()
    site_asr = models.IntegerField()
    site_location = models.CharField(max_length=255, default='Unknown')
    state_owned = models.BooleanField(default=False)

    def __str__(self):
        return 'Site Name: {}    Site Id: {} \
                Site ASR: {}     Site Location: {} '.format(
                                                                self.site_name,
                                                                self.site_id,
                                                                self.site_asr,
                                                                self.site_location,
                                                                )
    class Meta:
        managed = True
        db_table = 'site'
