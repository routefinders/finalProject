from django.conf.urls import patterns, include, url
from dps.views import *
from django.views.generic import ListView,DetailView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	
     #url(r'^$', 'mysite.views.home', name='home'),
	url(r'^contact_us/$',contactus ),
	url(r'^toKmeans/$',toKmeans),
    url(r'^testprint/$',TakeForm ),
    url (r'^$',landing),
	url (r'^logout/$',logout),
	url (r'^to_json/$',to_json),
	#url(r'^$',login),
    url(r'^admin/', include(admin.site.urls)),
    url (r'^dps/',include('dps.urls')),
	
)
