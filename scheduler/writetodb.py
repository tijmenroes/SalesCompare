import pymongo
from datetime import datetime
import json

import sys
sys.path.append('../')
from api_basic.views import write_to_db
# from api_basic.models import Date



def write():
    date = datetime.now()
    
    # client=pymongo.MongoClient('mongodb://127.0.0.1:27017')
    # mydb=client["prijsvergelijker"]
    # table= mydb.test

    poepdata = [{"title": "Superlit", "subtitle": "subtitle"}, {"title":  "Superlit2", "subtitle": "subtitle2"}]
    dump = json.dumps(poepdata)
    loaded = json.loads(dump)
    scraped_data = {"date": datetime.now(), "entries": loaded}

    write_to_db(scraped_data)




    # print(scraped_data)
    # table.insert_one(scraped_data)


    # json_string = {"date": date.strftime("%d/%m/%Y %H:%M:%S") ,"entries": [{"id": 0, "data": scraped_data} ]} 
    # json_string = '{"date": 1}'
    # serializer = dateSerializer()
    # print(json.dumps(json_string))
    
    # data = json.dumps(json_string)
    
    # data = JSONParser().parse(dumped)
 
# write()