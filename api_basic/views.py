import os
from datetime import datetime
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from django.conf import settings
from .models import Supermarket, Scraper,  Entry, Name, Info, ScraperEntry
from .serializers import SupermarketSerializer, dateSerializer, testSerializer, nameSerializer, ScraperSerializer, SupermarketDataSerializer
from scheduler import testscrapers


def get_supermarkets(request):
    if request.method == 'GET':
        supermarkets = Supermarket.objects.all()
        serializer = SupermarketSerializer(supermarkets, many=True)
        return JsonResponse(serializer.data, status=201)


@csrf_exempt
def add_supermarket(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SupermarketSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def write_to_db(sm_id, data):

    #   Try # 3
    scraped_mock_data = [
        {"title": "Croissantjes", "subtitle":  "nu 5 voor 1 euro",
            "old_price": "1.50", "new_price": "1", "img_path": 'NULL', },
        {"title": "Kaiserbroodjes", "subtitle":  "nu 6 voor 1 euro",
            "old_price": "1.70", "new_price": "1", "img_path": 'NULL', },
    ]
    # supermarket = Supermarket.objects.get(name="Jumbo")
    # print(supermarket._id)
    # s = ScraperEntry(supermarket = supermarket, time_start = datetime.now(), time_end =datetime.now(), sales = scraped_mock_data)
    # s.save()
    # print(s.supermarket)

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

        #  Er is misschien een betere manier door de entries op te halen en te groupen per supermarkt.
        supermarkets = Supermarket.objects.all()
        array = []

        for supermarket in supermarkets:
            data = ScraperEntry.objects.filter(supermarket=supermarket._id)
            entry = {"name": supermarket.name, "data": data}
            array.append(entry)

        serializer = SupermarketDataSerializer(array, many=True)
        return JsonResponse(serializer.data, status=201, safe=False)

    if request.method == 'POST':
        return HttpResponse("lolz")


@csrf_exempt
def run_scraper_manually(request):

    if request.method == 'POST':
        json_data = json.loads(request.body)
        sm_name = json_data['supermarket'].capitalize()
        print(sm_name)
        sm_id = Supermarket.objects.get(name=sm_name)
        # try:
        data = testscrapers.main(sm_name)
        for key in data:
            s = ScraperEntry(supermarket=sm_id, time_start=key["time_start"],
                                 time_end=key["time_end"], sales=key["sales"])
            s.save()
            print(s)
                  # print(s)

        return JsonResponse(data, safe=False)
        # except:
            # return HttpResponse("This scraper is not working")


@csrf_exempt
def get_entry(request):
    if request.method == 'GET':
        entries = Entry.objects.all()
        print(entries[0].headline)
        serializer = testSerializer(data=entries, many= True)

        if serializer.is_valid():
            print(serializer.data)
            return JsonResponse(serializer.data, status=201, safe=False)
        else:
            return HttpResponse(serializer.errors)

    if request.method == 'POST':
        return HttpResponse("lolz")


@csrf_exempt
def get_name(request):
    if request.method == 'GET':
        names = Name.objects.all()
        serializer = nameSerializer(names, many=True)

        return JsonResponse(serializer.data, status=201, safe=False)
        # else:
        #     return JsonResponse(serializer.errors)

    if request.method == 'POST':
        return HttpResponse("lolz")


@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        dates = Date.objects.all()
        print(dates[0])
        serializer = dateSerializer(dates, many=True)
        # print(serializer.data[1]["entries"][0])
        return JsonResponse(serializer.data, safe=False)
