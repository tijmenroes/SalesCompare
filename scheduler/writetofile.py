import os
from django.conf import settings
from datetime import datetime

def write():
    date = datetime.now()
    txtfile = open(os.path.join(settings.BASE_DIR, "textfile.txt"), "a")
    txtfile.write("\n ")
    txtfile.write(date.strftime("%d/%m/%Y %H:%M:%S") )
                
    # txtfile = open(os.path.join(settings.BASE_DIR, "textfile.txt"), "r")
    # read = txtfile.read()