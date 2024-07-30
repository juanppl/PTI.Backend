from django.urls import path
from categories.views import get_all_categories


urlpatterns = [
    path('get-list-of-categories/', get_all_categories)
]