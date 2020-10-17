from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from scheduler import writetofile
# from scheduler import scheduler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(writetofile.write, 'interval', minutes=1)
    scheduler.start()
    # /    # writetofile.write()