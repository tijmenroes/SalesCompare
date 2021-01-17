from rest_framework import serializers
from .models import Supermarket, Scraper

class SalesSerializer(serializers.Serializer):
    title = serializers.CharField()
    subtitle = serializers.CharField()
    old_price = serializers.CharField()
    new_price = serializers.CharField()
    img_path = serializers.CharField()

class ScraperSerializer(serializers.Serializer):
    time_start = serializers.DateField()
    time_end = serializers.DateField()
    sales = serializers.ListField(child=SalesSerializer())

class ScraperLogsSerializer(serializers.Serializer):
    scraper_id = serializers.CharField()
    supermarket = serializers.CharField()
    date_time = serializers.DateTimeField()
    amount_sales = serializers.IntegerField()
    succeeded = serializers.BooleanField()

class SupermarketSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Supermarket
        fields = ['name']
    
class SupermarketDataSerializer(serializers.Serializer):
    name =  serializers.CharField()
    data =  serializers.ListField(child=ScraperSerializer())
    
