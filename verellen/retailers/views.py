from django.shortcuts import render, redirect
from django.db.models import Q
import re

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
        array = []
        for s in split:
            s = s.replace(',', '').strip()
            if len(s) > 2 and not s.isdigit():
                array.append(s)

        if len(array) > 0:
            regex = '^.*(%s).*$' % '|'.join(array)

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
        else:
            matches = Retailer.objects.filter(Q(partner__name__contains=query)
                                          | Q(address__contains=query)
                                          | Q(city__contains=query)
                                          | Q(phone__contains=query)
                                          | Q(state__contains=query)
                                          | Q(zip_code__contains=query)
                                          )

    # If it is the case there are no matches we try to do a more greedy search by splitting the query even more
    if len(matches) < 1:
        split = re.findall(r'[,\w]+', query)
        array = []
        for s in split:
            s = s.replace(',', '').strip()
            if len(s) > 2 and not s.isdigit():
                array.append(s)
        if array and len(array) > 0:
            regex = '^.*(%s).*$' % '|'.join(array)
            matches = Retailer.objects.filter(Q(partner__name__iregex=regex)
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
