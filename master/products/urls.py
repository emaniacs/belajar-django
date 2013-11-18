from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'products.views.home'),
    
    url(r'^beli/$', 'products.views.beli'),
    url(r'^add/$', 'products.views.add'),
    url(r'^checkout/$', 'products.views.checkout'),
    url(r'^checkouts/$', 'products.views._tmp'),
    
    url(r'^by/(?P<item_type>\w+)/$', 'products.views.by_type'),
    
    url(r'^by/(?P<item_type>\w+)/(?P<item_id>\d+)/(?P<item_name>.*)/$', 'products.views.by_type_detail'),
    url(r'^by/(?P<item_type>\w+)/(?P<item_id>\d+)/$', 'products.views.by_type_detail'),
)
