from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'products.views.home'),
    url(r'^detail/(?P<item_id>\d+)/$', 'products.views.detail'),
    
    url(r'^beli/(?P<item_id>\d+)/$', 'products.views.beli'),
    
    url(r'^by/(?P<item_type>\w+)/$', 'products.views.by_type'),
    
    url(r'^by/(?P<item_type>\w+)/(?P<item_id>\d+)/(?P<item_name>.*)/$', 'products.views.by_type_detail'),
    url(r'^by/(?P<item_type>\w+)/(?P<item_id>\d+)/$', 'products.views.by_type_detail'),
)
