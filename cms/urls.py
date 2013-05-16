from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': 'C:/cms/cms/js/tiny_mce/' }),
	
	url(r'^search/$', 'cms.search.views.search'),
	
	url(r'^weblog/', include('coltrane.urls.entries')),	
	
	url(r'^weblog/links/', include('coltrane.urls.links')),	
	
	url(r'^weblog/tags/', include('coltrane.urls.tags')),

	url(r'^weblog/categories/', include('coltrane.urls.categories')),		
)
