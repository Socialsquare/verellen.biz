from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from products import views as product_views

urlpatterns = patterns('',

    url(r'^products/$', product_views.index, name='product.index'),
    url(r'^product/(?P<product_id>\d+)$', product_views.detail, name='product.detail'),

    (r'^', include('django.contrib.flatpages.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
