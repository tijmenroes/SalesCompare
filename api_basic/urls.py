from django.urls import path
from .views import   get_supermarkets, add_supermarket, get_scraper_entry, run_scraper_manually
urlpatterns = [
    path('api/supermarkets', get_supermarkets),
    path('api/add-supermarket', add_supermarket),
    path('api/getscraperentries', get_scraper_entry),
    path('api/runscraper', run_scraper_manually),
]