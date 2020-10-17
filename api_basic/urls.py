from django.urls import path
from .views import article_list, article_detail, write_to_file
urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>/', article_detail),
    path('text/', write_to_file)
]