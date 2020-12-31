from django.db import models
from user.models import User

class Note(models.Model):
    user =  models.ForeignKey(User, on_delete=models.DO_NOTHING)
    submitted_note = models.CharField(max_length=1000)

    class Meta:
        managed = True;
        db_table = 'note'

    def __str__(self):
        return f'Subject:{self.user}  Note:{self.submitted_note}'
