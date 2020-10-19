from django.urls import path
from .views import  write_to_file, get_supermarkets, add_supermarket, get_data
urlpatterns = [
    path('api/supermarkets', get_supermarkets),
    path('api/add-supermarket', add_supermarket),
    path('api/getdata', get_data),
    path('text/', write_to_file)
]