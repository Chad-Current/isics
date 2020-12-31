from django.apps import AppConfig


class AlarmConfig(AppConfig):
    name = 'alarm'
    
    def ready(self):
        import alarm.signals
