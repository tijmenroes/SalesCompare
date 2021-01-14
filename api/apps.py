from django.apps import AppConfig


class ApiBasicConfig(AppConfig):
    name = 'api'

    def ready(self):
        from scheduler import scheduler
        scheduler.start()