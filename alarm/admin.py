from django.contrib import admin
from .models import Alarm, AlarmComment, AlarmArchive

admin.site.register(Alarm)
admin.site.register(AlarmComment)
admin.site.register(AlarmArchive)
