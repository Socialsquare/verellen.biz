import urllib
import json
from django.db import models

class Retailer(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200, blank=True, null=True)
    zip_code = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200)
    website = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)

    lat = models.FloatField()
    lng = models.FloatField()

    def __unicode__(self):
        return self.name

    def save(self):
        location = "%s, %s, %s, %s" % (self.address, self.city, self.state, self.zip_code)

        #if not self.lat or not self.lng:
        latlng = self.geocode(location)
        self.lat = latlng[0]
        self.lng = latlng[1]

        super(Retailer, self).save()

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
