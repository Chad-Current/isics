from django.contrib import admin
from .models import Email, EmailTo, Sitemaintenance

admin.site.register(Email)
admin.site.register(Sitemaintenance)
admin.site.register(EmailTo)
