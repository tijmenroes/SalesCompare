from django.urls import path
from .views import   get_supermarkets, add_supermarket, get_data, get_entry, get_name, get_scraper_entry
urlpatterns = [
    path('api/supermarkets', get_supermarkets),
    path('api/add-supermarket', add_supermarket),
    path('api/getdata', get_data),
    path('api/getentry', get_entry),
    path('api/getname', get_name),
    path('api/getscraperentries', get_scraper_entry),
]