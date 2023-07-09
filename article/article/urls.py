from django.contrib import admin
from django.urls import path
from board.views import add_search_term, search_terms, show_crawling_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search-terms/', search_terms, name='search_terms'),
    path('add-search-term/', add_search_term, name='add_search_term'),
    path('crawling-info/<int:term_id>/', show_crawling_info, name='show_crawling_info'),
]
