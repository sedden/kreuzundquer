from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap

# Admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
)

# Debug? Serve static files.
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
        (r'^contact/', include('contact_form.urls')),
    )

# Blog
if 'blog' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^blog/', include('blog.urls')),
    )

# Sitemaps
sitemaps = { 
	'flatpages': FlatPageSitemap, 
#	'blog': GenericSitemap(archive_common, priority=0.8),
}
if 'django.contrib.sitemaps' in settings.INSTALLED_APPS:
	urlpatterns += patterns('',
		(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

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

