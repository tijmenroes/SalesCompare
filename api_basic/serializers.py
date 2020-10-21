from rest_framework import serializers
from .models import Supermarket, Scraper, Entry, Author

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


class SupermarketSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Supermarket
        fields = ['id', 'name', 'active']
    

# All my try's 

class entriesSerializer(serializers.ModelSerializer):
        class Meta:
            model = Entry
            fields = ['title', 'subtitle']


class dateSerializer(serializers.ModelSerializer): 
        
    entries = entriesSerializer(many=True)

    class Meta:
        model = Scraper        
        fields = ['id', 'date', 'entries']


class authorSerializer(serializers.Serializer):
    name = serializers.CharField()
    # class Meta:
        # model = Author
        # fields = ['name', 'email']        

class testSerializer(serializers.Serializer):
    # authors = authorSerializer(many=True)
    headline = serializers.CharField()
    authors = serializers.ListField(child=authorSerializer())
    # class Meta:
        # model = Entry
        # fields = ['headline']


class infoSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    sex = serializers.CharField()
    # class Meta:
        # fields = ['age', 'sex']

class nameSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    # info = infoSerializer(many=True)
    info = serializers.ListField(child=infoSerializer())
    # class Meta:
        # fields = ['firstname', 'info']


