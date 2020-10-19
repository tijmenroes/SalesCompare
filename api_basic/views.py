from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Supermarket, Date
from .serializers import SupermarketSerializer, dateSerializer
from django.views.decorators.csrf import csrf_exempt

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






@csrf_exempt
def write_to_file(request):
    
    if request.method == 'GET':
        txtfile = open(os.path.join(settings.BASE_DIR, "textfile.txt"), "r")
        read = txtfile.read()
        return HttpResponse(read)
        

    elif request.method == 'POST':
        date = datetime.now()
        txtfile = open(os.path.join(settings.BASE_DIR, "textfile.txt"), "a")
        txtfile.write("\n hello ")
        txtfile.write(date.strftime("%d/%m/%Y %H:%M:%S") )
            
        txtfile = open(os.path.join(settings.BASE_DIR, "textfile.txt"), "r")
        read = txtfile.read()
        return HttpResponse(read)



def write_to_db(data):
    print(data['entries'])

    # dump = json.dumps(b)
    # print(type(json.loads(dump)))
    # e = Date(data)
    # e.save()
    # print(e.objects)
    serializer = dateSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
    else:
         print(serializer.errors)

@csrf_exempt
def get_data(request):
    if request.method == 'GET':
        dates = Date.objects.all()
        print(dates[0])
        serializer = dateSerializer(dates, many = True)
        # print(serializer.data[1]["entries"][0])
        return JsonResponse(serializer.data,status=201, safe=False)








# @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def article_detail(request,pk):
#     try: 
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
        
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method ==  'DELETE': 
#         article.delete()
#         return HttpResponse(status=204)









