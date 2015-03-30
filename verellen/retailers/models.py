import urllib
import json
from django.db import models

from partner.models import Partner

class Retailer(models.Model):
    partner = models.OneToOneField(Partner)

    address = models.CharField(max_length = 200)
    address2 = models.CharField(max_length = 200, blank=True, default="")
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200, blank=True, default="")
    zip_code = models.CharField(max_length = 200, blank=True, default="")
    country = models.CharField(max_length = 200)

    website = models.CharField(max_length = 200, blank=True, default="")
    phone = models.CharField(max_length = 200, blank=True, default="")

    lat = models.FloatField()
    lng = models.FloatField()

    localities = models.CharField(max_length = 400, blank=True, default="")

    def __unicode__(self):
        return self.partner.name

    def save(self, *args, **kwargs):
        location = "%s, %s, %s, %s" % (self.address, self.city, self.state, self.zip_code)

        #if not self.lat or not self.lng:
        latlng = self.geocode(location)
        self.lat = latlng[0]
        self.lng = latlng[1]

        localities = get_localities(self.lat, self.lng)
        print localities
        [localities.append(i) for i in get_localities(self.lat + 0.1, self.lng + 0.1) if i not in localities and self.address and self.city and self.state]
        [localities.append(i) for i in get_localities(self.lat - 0.1, self.lng + 0.1) if i not in localities and self.address and self.city and self.state]
        [localities.append(i) for i in get_localities(self.lat + 0.1, self.lng - 0.1) if i not in localities and self.address and self.city and self.state]
        [localities.append(i) for i in get_localities(self.lat - 0.1, self.lng - 0.1) if i not in localities and self.address and self.city and self.state]
        print localities
        if len(localities) > 0:
            self.localities = ' '.join([str(x) for x in localities])

        super(Retailer, self).save(*args, **kwargs)

    def geocode(self, location):
        location = urllib.quote_plus(location)

        request = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % (location)
        data = urllib.urlopen(request).read()

        dataj = json.loads(data)

        if dataj['status'] != 'OK':
            return (0, 0) # fail

        geo = dataj['results'][0]['geometry']
        loc = geo['location']
        return (loc['lat'], loc['lng'])
        # dlist = data.split(',')
        # if dlist[0] == '200':
        #     return "%s,%s" % (dlist[2], dlist[3])
        # else:
        #     return ','

def get_localities(lat, lng):
    request = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=false" % (lat, lng)
    print request
    data = urllib.urlopen(request).read()
    dataj = json.loads(data)
    localities = []
    if dataj['status'] == 'OK':
        for r in dataj['results']:
            if 'postcode_localities' in r:
                localities = r['postcode_localities']
                break

    return localities

# class VerellenBoutiques(models.Model):
#     name = models.CharField(max_length = 200)
#     address = models.CharField(max_length = 200)
#     address2 = models.CharField(max_length = 200, blank=True, default="")
#     city = models.CharField(max_length = 200)
#     state = models.CharField(max_length = 200, blank=True, default="")
#     zip_code = models.CharField(max_length = 200, blank=True, default="")
#     country = models.CharField(max_length = 200)
#     phone = models.CharField(max_length = 200, blank=True, default="")

#     lat = models.FloatField()
#     lng = models.FloatField()

#     localities = models.CharField(max_length = 200, blank=True, default="")

#     def __unicode__(self):
#         return self.name

#     class Meta:
#         verbose_name_plural = "Verellen Boutiques"