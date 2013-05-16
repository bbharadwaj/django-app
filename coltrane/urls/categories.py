from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from coltrane.models import Category
from django.views.generic.date_based import object_detail, archive_day,archive_month,archive_year, archive_index



urlpatterns = patterns('',
	(r'^$','django.views.generic.list_detail.object_list', { 'queryset': Category.objects.all() }),
	(r'^(?P<slug>[-\w]+)/$','coltrane.views.category_detail'),
)

