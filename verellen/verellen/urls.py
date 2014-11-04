from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from products import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^product/(?P<product_id>\d+)$', views.detail, name='detail'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^pages/', include('django.contrib.flatpages.urls')),
)
