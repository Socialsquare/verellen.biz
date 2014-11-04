from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from products import views as product_views
from retailers import views as retailer_views

urlpatterns = patterns('',
    url(r'^retailers/$', retailer_views.index, name='retailer.index'),
    url(r'^retailers/(?P<address>.+)$', retailer_views.search, name='retailer.search'),

    url(r'^products/$', product_views.index, name='product.index'),
    url(r'^product/(?P<product_id>\d+)$', product_views.detail, name='product.detail'),

    # flatpages

    url(r'^admin/', include(admin.site.urls)),
)
