from django.db import models

class IsicApplicant(models.Model):
    primary_key = models.BigIntegerField(primary_key=True)
    applicant = models.CharField(max_length=255, null=False)
    loi = models.BooleanField(default=False)
    moa = models.BooleanField(default=False)
    part_pl = models.BooleanField(default=False)
    ugc = models.BooleanField(default=False)
    isicsb_approved = models.BooleanField(default=False)
    user_level = models.SmallIntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'applicants'
