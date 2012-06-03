from django.conf.urls.defaults import *

from blog.models import Entry

archive_common = {
	'queryset': Entry.objects.filter(is_public=True),
	'date_field': 'date',
}

urlpatterns = patterns('django.views.generic.date_based',
	(r'^(?P<year>\d{4})/$', 'archive_year',
		dict(archive_common, make_object_list=True),
	),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_month',
		dict(archive_common, month_format='%m'),
	),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'archive_day',
		dict(archive_common, month_format='%m', day_format='%d' ),
	),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>.*)/$', 'object_detail',
		dict(archive_common, queryset=Entry.objects.all(), month_format='%m', day_format='%d', slug_field='slug', ),
	),
)

urlpatterns += patterns('django.views.generic.list_detail',
    (r'^page/(?P<page>\d+)/$', 'object_list',
         { 'queryset':archive_common['queryset'], 'paginate_by':5,  },
        ),
    (r'^$', 'object_list',
         { 'queryset':archive_common['queryset'], 'paginate_by':5, 'page':0 },
        ),
)


urlpatterns += patterns('tagging.views',
	(r'^(?P<tag>.*)/$', 'tagged_object_list', {
		'queryset_or_model': Entry,
		'related_tags': True,
		'template_name': 'blog/entry_list_tags.html',
	 } ),
)
