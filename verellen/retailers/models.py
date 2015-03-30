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

    localities = models.CharField(max_length = 200, blank=True, default="")

    def __unicode__(self):
        return self.partner.name

    def save(self, *args, **kwargs):
        location = "%s, %s, %s, %s" % (self.address, self.city, self.state, self.zip_code)

        #if not self.lat or not self.lng:
        latlng = self.geocode(location)
        self.lat = latlng[0]
        self.lng = latlng[1]

        request = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=false" % (self.lat, self.lng)
        data = urllib.urlopen(request).read()
        dataj = json.loads(data)
        localities = []
        if dataj['status'] == 'OK':
            for r in dataj['results']:
                if 'postcode_localities' in r:
                    localities = r['postcode_localities']
                    break

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
