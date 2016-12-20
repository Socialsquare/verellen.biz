from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView

from products import views as product_views
from retailers import views as retailer_views
from partner import views as partner_views
from content import views as content_views

urlpatterns = [
    url(r'^$', content_views.landing, name='content.landing'),
    url(r'^home$', content_views.home, name='content.home'),
    url(r'^robots.txt/$', content_views.robots, name='content.robots'), # TODO: wat

    url(r'^retailers/$', retailer_views.home, name='retailer.home'),

    url(r'(pdfjs/web/viewer\.html.*)$', TemplateView.as_view(template_name='pdfjs/web/viewer.html')),

    url(r'^partner/$', partner_views.home, name='partner.home'),
    url(r'^partner/home/$', partner_views.home, name='partner.home'),
    url(r'^partner/search/$', partner_views.search, name='partner.search'),
    url(r'^partner/login/$', partner_views.do_login, name='partner.login'),
    url(r'^partner/logout/$', partner_views.do_logout, name='partner.logout'),
    url(r'^partner/login_form$', partner_views.login_form, name='partner.login_form'),

    url(r'^partner/products$', partner_views.product_category_list, name='partner.product_category_list'),
    url(r'^partner/products/(?P<category_slug>.*)$', partner_views.product_category, name='partner.product_category'),
    url(r'^partner/product/(?P<product_id>.*)$', partner_views.product_detail, name='partner.product_detail'),

    url(r'^partner/download/us$', partner_views.download_products_us, name='partner.download_products_us'),
    url(r'^partner/download/eu$', partner_views.download_products_eu, name='partner.download_products_eu'),

    url(r'^partner/download/us/(?P<category_slug>.*)$', partner_views.download_categories_us, name='partner.download_categories_us'),
    url(r'^partner/download/eu/(?P<category_slug>.*)$', partner_views.download_categories_eu, name='partner.download_categories_eu'),

    url(r'^partner/price_lists$', partner_views.price_lists, name='partner.price_lists'),
    url(r'^partner/sales_tools$', partner_views.sales_tools, name='partner.sales_tools'),
    url(r'^partner/account/$', partner_views.account, name='partner.account'),
    url(r'^partner/account_update/$', partner_views.account_update, name='partner.account_update'),
    url(r'^partner/view$', partner_views.view_spreadsheet, name='partner.view_spreadsheet'),

    url(r'^products/$', product_views.home, name='product.home'),
    url(r'^products/(?P<category_slug>.*)$', product_views.list, name='product.list'),
    url(r'^product/(?P<product_id>\d+)$', product_views.detail, name='product.detail'),

    url(r'^about/$', content_views.about, name='content.about'),

    url(r'^tinymce/', include('tinymce.urls')),

    # administration
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
