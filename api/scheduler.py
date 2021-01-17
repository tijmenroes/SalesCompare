from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .views import save_scraper_data
from .models import Supermarket

scheduler = BackgroundScheduler()
supermarkets = Supermarket.objects.all()

def runscrapers():
    for s in supermarkets:
        save_scraper_data(s, True)

def testscrapers():
    for s in supermarkets:
        save_scraper_data(s, False)

def start():
    scheduler.add_job(runscrapers, 'cron', day_of_week='mon', hour=6, jitter=3600)
    scheduler.add_job(testscrapers, 'cron', day_of_week='wed,fri,sun', hour=4, jitter=3600)
    scheduler.start()
 


