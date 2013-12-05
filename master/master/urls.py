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

    url(r'^_/', include(admin.site.urls)),
     
    # /PRODUK/*
    #~ url(r'^produk/', include('products.urls')),
    url(r'^produk/$', 'products.views.home'),
    
    url(r'^produk/beli/$', 'products.views.beli'),
    url(r'^produk/add/$', 'products.views.add'),
    url(r'^produk/checkout/$', 'products.views.checkout'),
    url(r'^produk/checkouts/$', 'products.views._tmp'),
    
    url(r'^produk/by/pembayaran/$', 'pembayaran.views.home'),
    url(r'^produk/by/(?P<item_type>\w+)/$', 'products.views.by_type'),
    
    url(r'^produk/by/(?P<item_type>\w+)/(?P<item_id>\d+)/(?P<item_name>.*)/$', 'products.views.by_type_detail'),
    url(r'^produk/by/(?P<item_type>\w+)/(?P<item_id>\d+)/$', 'products.views.by_type_detail'),
     
     
    # /STATS/*
    url(r'^stats/', 'stats.views.home'),

    # PENJUALAN
    url(r'^penjualan/$', 'penjualan.views.home'),
    url(r'^penjualan/hari-ini/$', 'penjualan.views.hari_ini'),
    url(r'^penjualan/(?P<tahun>\d{4})/$', 'penjualan.views.by_filter'),
    url(r'^penjualan/(?P<tahun>\d{4})/(?P<bulan>\d{1,2})/$', 'penjualan.views.by_filter'),
    url(r'^penjualan/(?P<tahun>\d{4})/(?P<bulan>\d{1,2})/(?P<hari>\d{1,2})/$', 'penjualan.views.by_filter'),
    
    url(r'^penjualan/(?P<t1>\d{4})-(?P<b1>\d{1,2})-(?P<h1>\d{1,2})/(?P<t2>\d{4})-(?P<b2>\d{1,2})-(?P<h2>\d{1,2})$', 'penjualan.views.by_range'),

    # PEMBAYARAN
    url(r'^pembayaran/$', 'pembayaran.views.home'),
    url(r'^pembayaran/(?P<tipe>\w+)/$', 'pembayaran.views.bayar'),
    
    # Ajax
    url(r'^ajax/pelanggan/$', 'ajax.views.pelanggan'),
)

handler404 = 'master.views.error404'
