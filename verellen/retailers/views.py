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
        if len(query) == 2:
            matches = Retailer.objects.filter(Q(state__icontains=query))
        else:
            matchObj = re.match(r'(.{2}),?\s+(USA|Canada)', query, flags=re.IGNORECASE)
            if matchObj:
                matches = Retailer.objects.filter(Q(state__icontains=matchObj.group(1)) & Q(country__icontains=matchObj.group(2)))

        if len(matches) == len(all) or len(matches) == 0:
            split = query.split(',')
            array = []
            for s in split:
                s = s.replace(',', '').strip()
                if len(s) > 1 and not s.isdigit():
                    array.append(s)

            if len(array) > 1:
                regex = '^.*(%s).*$' % '|'.join(array)

                matches = Retailer.objects.filter(Q(partner__name__icontains=query)
                                              | Q(address__icontains=query)
                                              | Q(city__icontains=query)
                                              | Q(phone__icontains=query)
                                              | Q(state__icontains=query)
                                              | Q(country__icontains=query)
                                              | Q(zip_code__icontains=query)
                                              | Q(localities__icontains=query)
                                              | Q(partner__name__iregex=regex)
                                              | Q(address__iregex=regex)
                                              | Q(city__iregex=regex)
                                              | Q(phone__iregex=regex)
                                              | Q(state__iregex=regex)
                                              | Q(zip_code__iregex=regex)
                                              | Q(localities__iregex=regex)
                                              )
            else:
                matches = Retailer.objects.filter(Q(partner__name__icontains=query)
                                              | Q(address__icontains=query)
                                              | Q(city__icontains=query)
                                              | Q(phone__icontains=query)
                                              | Q(state__icontains=query)
                                              | Q(country__icontains=query)
                                              | Q(zip_code__icontains=query)
                                              | Q(localities__icontains=query)
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
                                              | Q(localities__iregex=regex)
                                              )
    matches = matches.order_by('partner__name')
    return render(request, 'retailers/home.html', {
        'matches': matches,
        'retailers': matches,
        'search_query': query,
        'showing_all': showing_all
    })
