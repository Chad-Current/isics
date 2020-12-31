from django.apps import AppConfig


class TicketsystemConfig(AppConfig):
    name = 'ticketsystem'

    def ready(self):
        import ticketsystem.signals
