from jsonfield import JSONField
from djongo import models
from django import forms

class Supermarket(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, blank=False)
    active = models.BooleanField(default=True)

class Sale(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(blank=True, null=True)
    old_price = models.CharField(blank=True, null=True)
    new_price = models.CharField(blank=True, null=True)
    img_path = models.CharField(blank=True, null=True)
    
    class Meta:
        abstract = True

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ('title', 'subtitle', 'old_price', 'new_price', 'img_path')
        
class ScraperEntry(models.Model):
    _id = models.ObjectIdField()
    supermarket = models.ForeignKey('Supermarket', on_delete=models.PROTECT)   
    time_start = models.DateField(blank=True, null=True)
    time_end = models.DateField(blank=True, null=True) 
    sales = models.ArrayField(
        model_container=Sale,
        model_form_class=SaleForm
    )
    objects = models.DjongoManager()

class Scraper(models.Model):
    _id = models.ObjectIdField()
    date = models.DateTimeField(max_length=100, blank=False)
    supermarket_id = models.IntegerField(blank=False)

class ScraperLogs(models.Model):
    _id = models.ObjectIdField()
    scraper_id = models.ForeignKey('ScraperEntry', on_delete=models.PROTECT, blank= True, null=True)  
    supermarket = models.ForeignKey('Supermarket', on_delete=models.PROTECT)
    date_time = models.DateTimeField(auto_now_add=True, blank=False)
    amount_sales = models.IntegerField(default=0)
    succeeded = models.BooleanField(default=False)

    

