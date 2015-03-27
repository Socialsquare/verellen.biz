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
        split = query.split(',')
        regex = '^.*(%s).*$' % '|'.join(split)
        matches = Retailer.objects.filter(Q(partner__name__contains=query)
                                          | Q(address__contains=query)
                                          | Q(city__contains=query)
                                          | Q(phone__contains=query)
                                          | Q(state__contains=query)
                                          | Q(zip_code__contains=query)
                                          | Q(partner__name__iregex=regex)
                                          | Q(address__iregex=regex)
                                          | Q(city__iregex=regex)
                                          | Q(phone__iregex=regex)
                                          | Q(state__iregex=regex)
                                          | Q(zip_code__iregex=regex)
                                          )

    return render(request, 'retailers/home.html', {
        'matches': matches,
        'retailers': matches,
        'search_query': query,
        'showing_all': showing_all
    })
