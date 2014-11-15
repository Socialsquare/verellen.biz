from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from products import views as product_views
from retailers import views as retailer_views
from partner import views as partner_views
from content import views as content_views

urlpatterns = patterns('',
    url(r'^$', content_views.home, name='content.home'),

    url(r'^retailers/$', retailer_views.index, name='retailer.index'),
    url(r'^retailers/(?P<address>.+)$', retailer_views.search, name='retailer.search'),

    url(r'^partner/login/$', partner_views.do_login, name='partner.login'),
    url(r'^partner/logout/$', partner_views.do_logout, name='partner.logout'),
    url(r'^partner/login_form$', partner_views.login_form, name='partner.login_form'),
    url(r'^partner/index/$', partner_views.index, name='partner.index'),

    url(r'^products/$', product_views.list, name='product.list'),
    url(r'^product/(?P<product_id>\d+)$', product_views.detail, name='product.detail'),

    url(r'^about/$', content_views.about, name='content.about'),

    url(r'^tinymce/', include('tinymce.urls')),

    # administration
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
