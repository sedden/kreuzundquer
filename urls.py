from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap

# Admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

# Sitemaps, Feeds
sitemaps = { 'flatpages': FlatPageSitemap }
feeds = {}

# Debug? Serve static files!
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
           {
            'document_root': settings.PRJ_DIR+'/static',
            'show_indexes': True
	   }
        ),
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    )

# MarkItUp
if 'markitup' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^markitup/', include('markitup.urls')),
    )

# Contact
if 'contact_form' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^kontakt/', include('contact_form.urls')),
    )

# Robots
if 'robots' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^robots.txt$', include('robots.urls')),
    )

# Blog
if 'blog' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^blog/', include('blog.urls')),
    )
    from blog.urls import archive_common
    from blog.feeds import LatestEntriesRss, LatestEntriesAtom, LatestCommentsRss, LatestCommentsAtom
    sitemaps['blog'] = GenericSitemap(archive_common, priority=0.8)
    feeds['atom'] = LatestEntriesAtom
    feeds['rss'] = LatestEntriesRss
    feeds['comments-atom'] = LatestCommentsAtom
    feeds['comments-rss'] = LatestCommentsRss

# Registration
if 'django.contrib.auth' in settings.INSTALLED_APPS:
	urlpatterns += patterns('',
		(r'^login/$', 'django.contrib.auth.views.login'),
		(r'^logout/$', 'django.contrib.auth.views.logout'),
	)

# Comments
if 'django.contrib.comments' in settings.INSTALLED_APPS:
	urlpatterns += patterns('',
		(r'^comments/', include('django.contrib.comments.urls')),
	)

# Sitemaps
if 'django.contrib.sitemaps' in settings.INSTALLED_APPS:
	urlpatterns += patterns('',
		(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
	)

# Feeds
if 'django.contrib.syndication' in settings.INSTALLED_APPS:
	urlpatterns += patterns('',
		(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
	)
