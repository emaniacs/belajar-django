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
    # url(r'^master/', include('master.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^ambo/', include(admin.site.urls)),
     
     # /produk/*
     url(r'^produk/', include('products.urls')),
     
     # /stats/*
     url(r'^stats/', include('stats.urls')),
     
     
)

handler404 = 'master.views.error404'
