from django.db import models

class Generator(models.Model):
    gen_location = models.CharField(max_length=255)
    gen_address = models.CharField(max_length=255)
    gen_cost = models.CharField(max_length=255)
    gen_contract = models.CharField(max_length=50)
    gen_vendor = models.CharField(max_length=50)
    gen_poc = models.CharField(max_length=100)
    gen_phonenumber = models.CharField(max_length=25)
    gen_email = models.EmailField(max_length=255)

    class Meta:
        managed = True
        db_table = 'generator'

    def __str__(self):
        return f'{self.gen_location}{self.gen_address}'


