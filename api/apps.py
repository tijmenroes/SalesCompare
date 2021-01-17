from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler

class ApiBasicConfig(AppConfig):
    name = 'api'

    def ready(self):
        from api import scheduler
        scheduler.start()