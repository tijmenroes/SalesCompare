from django.urls import path
from .views import   get_supermarkets, add_supermarket, get_sales, get_scraper_entry, run_scraper_manually
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='SalesCompare API')

urlpatterns = [
    path('api/supermarkets', get_supermarkets),
    path('api/add-supermarket', add_supermarket),
    path('api/getscraperentries', get_scraper_entry),
    path('api/getsales', get_sales),
    path('api/runscraper', run_scraper_manually),
    path('api/swagger', schema_view)
]