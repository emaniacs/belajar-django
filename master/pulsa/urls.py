from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'pulsa.views.home'),
    url(r'^detail/$', 'pulsa.views.detail'),
    url(r'^detail/(?P<pulsa_id>\d+)/$', 'pulsa.views.detail'),
    
    url(r'^beli/$', 'pulsa.views.beli'),
    url(r'^beli/(?P<pulsa_id>\d+)/$', 'pulsa.views.beli'),
)
