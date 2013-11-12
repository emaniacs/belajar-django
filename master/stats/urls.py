from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'stats.views.home'),
    url(r'^detail/$', 'pulsa.views.detail'),
)
