from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'master.views.home', name='home'),
    # url(r'^master/', include('master.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^ambo/', include(admin.site.urls)),
     
     # /pulsa/*
     url(r'^pulsa/', include('pulsa.urls'))
)

handler404 = 'master.views.error404'
