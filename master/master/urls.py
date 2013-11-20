from django.conf.urls import patterns, include, url, handler404

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'master.views.home', name='home'),
    
     # login and logout
    url(r'^login/$', 'master.views.llogin', name='login'),
    url(r'^logout/$', 'master.views.llogout', name='logout'),

    url(r'^ambo/', include(admin.site.urls)),
     
    # /PRODUK/*
    #~ url(r'^produk/', include('products.urls')),
    url(r'^produk/$', 'products.views.home'),
    
    url(r'^produk/beli/$', 'products.views.beli'),
    url(r'^produk/add/$', 'products.views.add'),
    url(r'^produk/checkout/$', 'products.views.checkout'),
    url(r'^produk/checkouts/$', 'products.views._tmp'),
    
    url(r'^produk/by/(?P<item_type>\w+)/$', 'products.views.by_type'),
    
    url(r'^produk/by/(?P<item_type>\w+)/(?P<item_id>\d+)/(?P<item_name>.*)/$', 'products.views.by_type_detail'),
    url(r'^produk/by/(?P<item_type>\w+)/(?P<item_id>\d+)/$', 'products.views.by_type_detail'),
     
     
    # /STATS/*
    url(r'^stats/', 'stats.views.home'),

    # PENJUALAN
    url(r'^penjualan/$', 'penjualan.views.home'),
    url(r'^penjualan/hari-ini/$', 'penjualan.views.hari_ini'),

    # PEMBAYARAN
    url(r'^pembayaran/$', 'pembayaran.views.home'),
    url(r'^pembayaran/(?P<tipe>\w+)/$', 'pembayaran.views.bayar'),
)

handler404 = 'master.views.error404'
