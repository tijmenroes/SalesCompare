from jsonfield import JSONField
# from django.db import models
from djongo import models
from django import forms
# from django.contrib.postgres.fields import ArrayField


class Sale(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.EmailField()
    old_price = models.CharField()
    new_price = models.CharField()
    img_path = models.CharField()
    
    class Meta:
        abstract = True

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('title', 'subtitle', 'old_price', 'new_price', 'img_path')
        

class ScraperEntry(models.Model):
    _id = models.ObjectIdField()
    supermarket_id = models.IntegerField()   
    time_start = models.DateField()
    time_end = models.DateField() 
    sales = models.ArrayField(
        model_container=Sale,
        model_form_class=SaleForm
    )
    
    objects = models.DjongoManager()


class Supermarket(models.Model):
    id = models.IntegerField(blank=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Scraper(models.Model):
    _id = models.ObjectIdField()
    date = models.DateTimeField(max_length=100, blank=False)
    supermarket_id = models.IntegerField(blank=False)


class Info(models.Model):
    age = models.CharField(max_length=200)
    sex = models.EmailField()
    
    class Meta:
        abstract = True

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = (
            'age', 'sex'
        )
        
class Name(models.Model):
    _id = models.ObjectIdField()
    firstname = models.CharField(max_length=255)    
    info = models.ArrayField(
        model_container=Info,
        model_form_class=InfoForm
    )
    
    objects = models.DjongoManager()






    

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    class Meta:
        abstract = True

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            'name', 'email'
        )
        
class Entry(models.Model):
    _id = models.ObjectIdField()
    date = models.DateTimeField()
    supermarket_id = models.IntegerField(blank = False)
    headline = models.CharField(max_length=255)    
    authors = models.ArrayField(
        model_container=Author,
        model_form_class=AuthorForm
    )
    
    objects = models.DjongoManager()
