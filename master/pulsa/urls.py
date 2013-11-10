from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'pulsa.views.home'),
    url(r'^detail/$', 'pulsa.views.detail'),
    url(r'^detail/(?P<pulsa_id>\d+)/$', 'pulsa.views.detail'),
    
    url(r'^remove/$', 'pulsa.views.remove'),
    url(r'^remove/(?P<pulsa_id>\d+)/$', 'pulsa.views.remove'),
    
    url(r'^edit/$', 'pulsa.views.edit'),
    url(r'^edit/(?P<pulsa_id>\d+)/$', 'pulsa.views.edit'),
    
    url(r'^add/$', 'pulsa.views.add'),
)
