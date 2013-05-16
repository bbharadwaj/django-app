from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from coltrane.models import Entry, Link, Category
from tagging.models import Tag
from django.views.generic.date_based import object_detail, archive_day,archive_month,archive_year, archive_index


urlpatterns = patterns('',
	(r'^$','django.views.generic.list_detail.object_list', { 'queryset': Tag.objects.all() }),
	(r'^entries/(?P<tag>[-\w]+)/$','tagging.views.tagged_object_list', { 'queryset_or_model': Entry,'template_name': 'coltrane/entries_by_tag.html' }),
	(r'^links/(?P<tag>[-\w]+)/$', 'tagging.views.tagged_object_list', { 'queryset_or_model': Link,'template_name': 'coltrane/links_by_tag.html' }),
)



