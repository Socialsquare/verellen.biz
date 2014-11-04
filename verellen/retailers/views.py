from django.shortcuts import render

from retailers.models import Retailer

def index(request):
    return render(request, 'retailers/index.html')

def search(request, address):
    # TODO: safe address
    matches = Retailer.objects.all()

    return render(request, 'retailers/search.html',
                  {
                      'matches': matches,
                      'search_query': address
                  })
