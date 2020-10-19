from rest_framework import serializers
from .models import Supermarket, Date, Entry

class SupermarketSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Supermarket
        fields = ['id', 'name', 'active']
    

class entriesSerializer(serializers.ModelSerializer):
        class Meta:
            model = Entry
            fields = ['title', 'subtitle']


class dateSerializer(serializers.ModelSerializer): 
        
    entries = entriesSerializer(many=True)

    class Meta:
        model = Date        
        fields = ['id', 'date', 'entries']
        

# KUNNEN WE EEN APARTE SERIALIZER MAKEN VOOR ALLEEN DE ENTRIES LOLZZZZZZZZZZZZZZZZZZZZZZZ





# class dateSerializer(serializers.Serializer):

#     date = serializers.DateTimeField()
#     entries = serializers.ListField(child=entriesSerializer())

#     def create(self, validated_data):
#     #     return Article.objects.create(validated_data)



#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     date = serializers.DateTimeField()    


    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.save()
    #     return instance


# ModelSerializer kan een volgende stap zijn
