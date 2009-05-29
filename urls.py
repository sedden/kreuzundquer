from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

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

# Rosetta? Rosetta!
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
)

# TinyMCE? TinyMCE!
if 'tinymce' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^tinymce/', include('tinymce.urls')),
    )

# MarkItUp? MarkItUp!
if 'markitup' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^markitup/', include('markitup.urls')),
    )

# Contact Form? Contact Form!
if 'contact_form' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^contact/', include('contact_form.urls')),
    )

# WikiWiki!
if 'wiki' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^wiki/', include('wiki.urls')),
    )

# Django Page CMS
if 'pages' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^pages/', include('pages.urls')),
    )
