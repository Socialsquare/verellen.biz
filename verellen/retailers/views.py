from django.shortcuts import render, redirect
from django.db.models import Q

from retailers.models import Retailer

def home(request):
    all = Retailer.objects.all()
    matches = all
    showing_all = True
    query = ""

    if 'query' in request.GET.keys():
        showing_all = False
        query = request.GET['query']
        matches = Retailer.objects.filter(Q(partner__name__contains=query)
                                          | Q(address__contains=query)
                                          | Q(city__contains=query)
                                          | Q(phone__contains=query)
                                          | Q(state__contains=query)
                                          | Q(zip_code__contains=query))

    return render(request, 'retailers/home.html', {
        'matches': matches,
        'retailers': matches,
        'search_query': query,
        'showing_all': showing_all
    })
