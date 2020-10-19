from jsonfield import JSONField
from django.db import models
# from django.contrib.postgres.fields import ArrayField


class Supermarket(models.Model):
    name = models.CharField(max_length=100, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    title  = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=100, blank=False)


class Date(models.Model):
    date = models.DateTimeField(max_length=100, blank=False)
    entries = models.ManyToManyField(Entry)
    # kkdata = models.ForeignKey(Entry, related_name='entries')

# class ItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()

# class ItemsSerializer(serializers.Serializer):
#     items = serializers.ListField(child=ItemSerializer())



    # def __str__(self):
    #     return self.date



# Article model example
# class Article(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title