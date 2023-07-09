from django.urls import path
from .views import search_terms, add_search_term, show_crawling_info

urlpatterns = [
    path('', search_terms, name='search_terms'),
    path('add-search-term/', add_search_term, name='add_search_term'),
    path('crawling-info/<int:term_id>/', show_crawling_info, name='show_crawling_info'),
]