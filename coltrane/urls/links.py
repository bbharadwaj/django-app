from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from coltrane.models import Entry, Link, Category
from tagging.models import Tag
from django.views.generic.date_based import object_detail, archive_day,archive_month,archive_year, archive_index



link_info_dict = {
	'queryset': Link.objects.all(),
	'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    
	url(r'^$', 'archive_index', link_info_dict,'coltrane_link_archive_index'),
	url(r'^(?P<year>\d{4})/$','archive_year',link_info_dict, 'coltrane_link_archive_year'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$','archive_month', link_info_dict, 'coltrane_link_archive_month'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','archive_day', link_info_dict, 'coltrane_link_archive_day'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','object_detail', link_info_dict, 'coltrane_link_detail'),
	
)

