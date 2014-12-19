from django.shortcuts import render
from django.db.models import Q

from retailers.models import Retailer

def index(request):
    return render(request, 'retailers/index.html')

def search(request, query):
    matches = Retailer.objects.filter(Q(name__contains=query)
                                      | Q(address__contains=query)
                                      | Q(zip_code__contains=query))

    return render(request, 'retailers/search.html', {
        'matches': matches,
        'retailers': Retailer.objects.all(),
        'search_query': query
    })
