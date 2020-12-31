from django.db import models
from django.contrib.auth.models import User
# Transfer to USER models, doesn't make sense in this model
User._meta.get_field('email')._unique = True
