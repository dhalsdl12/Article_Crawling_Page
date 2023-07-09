from django.contrib import admin
from board.views import add_search_term, search_terms, show_crawling_info
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
]
