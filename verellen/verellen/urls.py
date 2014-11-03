from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from verellen_web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
