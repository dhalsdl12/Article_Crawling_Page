from django.shortcuts import render, redirect, get_object_or_404
from .models import SearchTerm
from .article import start


def add_search_term(request):
    if request.method == 'POST':
        term = request.POST.get('term')
        SearchTerm.objects.create(term=term)

        return redirect('search_terms')
    return render(request, 'add_search_term.html')


def search_terms(request):
    terms = SearchTerm.objects.all()
    return render(request, 'search_terms.html', {'terms': terms})


def show_crawling_info(request, term_id):
    term = get_object_or_404(SearchTerm, pk=term_id)

    title, link = start(term.term)
    return render(request, 'crawling_info.html', 
                  {'term': term, 
                   'title_link': zip(title, link)})
