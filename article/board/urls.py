from django.urls import path
from .views import search_terms, add_search_term, show_crawling_info, delete_search_term

urlpatterns = [
    path('', search_terms, name='search_terms'),
    path('add-search-term/', add_search_term, name='add_search_term'),
    path('crawling-info/<int:term_id>/', show_crawling_info, name='show_crawling_info'),
    path('search-terms/<int:term_id>/delete/', delete_search_term, name='delete_search_term'),
]