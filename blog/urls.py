from django.conf.urls.defaults import *

from blog.models import Entry

archive_common = {
	'queryset': Entry.objects.filter(is_public=True),
	'date_field': 'date',
}

urlpatterns = patterns('django.views.generic.date_based',
	(r'^$', 'archive_index',
		dict(archive_common, num_latest=15),
	),
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
