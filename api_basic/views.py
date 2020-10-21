from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Supermarket, Scraper,  Entry, Name, Info, ScraperEntry
from .serializers import SupermarketSerializer, dateSerializer, testSerializer, nameSerializer, ScraperSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import os
from django.conf import settings
from datetime import datetime
import json 

def get_supermarkets(request):
    if request.method == 'GET':
        supermarkets = Supermarket.objects.all()
        serializer = SupermarketSerializer(supermarkets, many = True)
        return JsonResponse(serializer.data,status=201)

@csrf_exempt
def add_supermarket(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SupermarketSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)



def write_to_db(sm_id, data):
    
    #   Try # 3
    scraped_mock_data = [
        { "title": "Croissantjes", "subtitle":  "nu 5 voor 1 euro", "old_price": "1.50", "new_price": "1", "img_path": 'NULL', },
        { "title": "Kaiserbroodjes", "subtitle":  "nu 6 voor 1 euro", "old_price": "1.70", "new_price": "1", "img_path": 'NULL', },
    ]
    s = ScraperEntry(supermarket_id = 1, time_start = datetime.now(), time_end =datetime.now(), sales = scraped_mock_data)
    # s.save()

    
    #   Try # 2
    
    # print('lol')
    # entry = Entry()
    # entry.authors = [{'name': 'John', 'email': 'john@mail.com'},
    #                 {'name': 'Paul', 'email': 'paul@mail.com'}]
    # # entry.save()
    # print(entry)

    #    First Try

    # # supermarket = Supermarket.objects.get(id=sm_id)
    # print(supermarket.id)
    # s = Scraper(supermarket_id = supermarket.id, date = datetime.now())
    # s.save()
    # print("scraper_id = ")
    # print(s._id)
    # sm_serializer = SupermarketSerializer(data=supermarket)
    # if sm_serializer.is_valid():
        # print(sm_serializer.data)


  
@csrf_exempt
def get_scraper_entry(request):
    if request.method == 'GET':
        entries = ScraperEntry.objects.all()
        serializer = ScraperSerializer(entries, many = True)

        return JsonResponse(serializer.data,status=201, safe=False)

    if request.method == 'POST':
        return HttpResponse("lolz")




    # Some serializing try's 
@csrf_exempt
def get_entry(request):
    if request.method == 'GET':
        entries = Entry.objects.all()
        print(entries[0].headline)
        serializer = testSerializer(data= entries, many = True)

        if serializer.is_valid():
            print(serializer.data)
            print("IK HEB AIDS")
            return JsonResponse(serializer.data,status=201, safe=False)
        else:
            return HttpResponse(serializer.errors)

    if request.method == 'POST':
        return HttpResponse("lolz")


@csrf_exempt
def get_name(request):
    if request.method == 'GET':
        names = Name.objects.all()
        serializer = nameSerializer(names, many = True)

        return JsonResponse(serializer.data,status=201, safe=False)
        # else:
        #     return JsonResponse(serializer.errors)

    if request.method == 'POST':
        return HttpResponse("lolz")
        
    
@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        dates = Date.objects.all()
        print(dates[0])
        serializer = dateSerializer(dates, many = True)
        # print(serializer.data[1]["entries"][0])
        return JsonResponse(serializer.data, safe=False)
