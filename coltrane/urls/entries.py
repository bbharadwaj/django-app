from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from coltrane.models import Entry, Link, Category
from tagging.models import Tag
from django.views.generic.date_based import object_detail, archive_day,archive_month,archive_year, archive_index

entry_info_dict = {
	'queryset': Entry.objects.all(),
	'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    
	url(r'^$', 'archive_index', entry_info_dict,'coltrane_entry_archive_index'),
	url(r'^(?P<year>\d{4})/$','archive_year',entry_info_dict, 'coltrane_entry_archive_year'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$','archive_month', entry_info_dict, 'coltrane_entry_archive_month'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','archive_day', entry_info_dict, 'coltrane_entry_archive_day'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','object_detail', entry_info_dict, 'coltrane_entry_detail'),
	
)

