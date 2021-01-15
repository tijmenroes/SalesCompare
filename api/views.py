import os
from datetime import datetime
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from django.conf import settings
from .models import Supermarket, Scraper,  ScraperEntry
from .serializers import SupermarketSerializer, ScraperSerializer, SupermarketDataSerializer
from scheduler import testscrapers


def get_supermarkets(request):
    if request.method == 'GET':
        supermarkets = Supermarket.objects.all()
        serializer = SupermarketSerializer(supermarkets, many=True)
        return JsonResponse(serializer.data, status=201, safe=False)

@csrf_exempt
def add_supermarket(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SupermarketSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

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
        return HttpResponse("this route only accepts GET requests")

@csrf_exempt
def run_scraper_manually(request, to_save):

    if request.method == 'POST':
        json_data = json.loads(request.body)
        sm_name = json_data['supermarket'].capitalize()
        sm_id = Supermarket.objects.get(name=sm_name)
        # try:
        data = testscrapers.main(sm_name)
        for key in data:
            s = ScraperEntry(supermarket=sm_id, time_start=key["time_start"], time_end=key["time_end"], sales=key["sales"])
            if to_save = True:
                s.save()
            


        return JsonResponse(data, safe=False)
        # except:
            # return HttpResponse("This scraper is not working")

@csrf_exempt
def get_sales(request):
    if request.method == 'GET':
        #  Er is misschien een betere manier door de entries op te halen en te groupen per supermarkt.
            
        sale_array = []
        # check if filters are given, if not, give all supermarketes
        try:
            body = json.loads(request.body) 
            body["filters"]
            supermarkets = [Supermarket.objects.get(name=f) for f in body["filters"]]
        except:
            supermarkets = Supermarket.objects.all()

        for supermarket in supermarkets:
            data = ScraperEntry.objects.filter(supermarket=supermarket._id)
            entry = {"name": supermarket.name, "data": data}
            sale_array.append(entry)

        serializer = SupermarketDataSerializer(sale_array, many=True)
        return JsonResponse(serializer.data, status=201, safe=False)

    if request.method == 'POST':
        return HttpResponse("this route only accepts GET requests")
