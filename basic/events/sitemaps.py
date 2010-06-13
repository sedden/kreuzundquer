from django.contrib.sitemaps import Sitemap
from basic.events.models import EventTime
from datetime import datetime, timedelta

class EventTimeSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return EventTime.objects.filter(start__gte=(datetime.today() - timedelta(days=1)))

    def lastmod(self, obj):
        return obj.event.modified

