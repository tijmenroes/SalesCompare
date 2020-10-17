from django.apps import AppConfig


class ApiBasicConfig(AppConfig):
    name = 'api_basic'

    def ready(self):
        from scheduler import scheduler
        # writetofile.write()
        scheduler.start()