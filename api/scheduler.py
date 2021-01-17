from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .views import save_scraper_data
from .models import Supermarket

scheduler = BackgroundScheduler()
supermarkets = Supermarket.objects.all()
def start():
    print('started')
    testscrapers()
    runscrapers() 
    # scheduler.add_job(writetofile.write, 'interval', minutes=1)
    # scheduler.start()
 

def testscrapers():
    print('yeee')
    for s in supermarkets:
        print(s.name)
        print(save_scraper_data(s, False))
        print("done!!!")

def runscrapers():
    print('yeee222222')

# def save_data(sm_name):
#     data = testscrapers.main(sm_name)
#     sm_id = Supermarket.objects.get(name=sm_name) 
    
#     for key in data:
#         s = ScraperEntry(supermarket=sm_id, time_start=key["time_start"], time_end=key["time_end"], sales=key["sales"])
#         s.save()


# save_scraper_data()