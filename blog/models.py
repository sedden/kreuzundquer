from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from datetime import time, date, datetime
from time import strptime

from tagging.models import Tag
from tagging.fields import TagField

from blog.fields import MarkdownTextField

#from xmlrpc import dispatcher
#from pingback.client import ping_external_links, ping_directories
#from pingback import create_ping_func

class Entry(models.Model):
	
	title = models.CharField(_('title'), max_length=200)
	slug = models.SlugField(_('slug'), unique='True')
	date = models.DateTimeField(_('date/time submitted'))
	body = MarkdownTextField(_('content'))
	excerpt = MarkdownTextField(_('excerpt')) 

	enable_comments = models.BooleanField(_('enable comments'), default=True)
	is_public = models.BooleanField(_('is public'), default=True)

	tags = TagField()

	author = models.ForeignKey(User, editable=False, verbose_name=_('author'))

	class Meta:
		ordering = ['-date']
		verbose_name = 'Eintrag'
		verbose_name_plural = 'Eintraege'

	def get_absolute_url(self):
		return '/blog/%s/%s/' % ( self.date.strftime("%Y/%m/%d"), self.slug)

	def get_next_public_by_date(self):
		return self.get_next_by_date(is_public=True)

	def get_previous_public_by_date(self):
		return self.get_previous_by_date(is_public=True)

	def __unicode__(self):
		return u'%s' % self.title


# Pingback server
#dispatcher.register_function(create_ping_func, 'pingback.ping')

# Pingback clients
#ping_dirs = ping_directories(
#	content_attr='body_html',
#	url_attr='get_absolute_url',
#	filtr=lambda x: x.is_public,
#	feed_url_fun=lambda x: reverse('django.contrib.syndication.views.feed', args=['atom'])
#)
#models.signals.post_save.connect(ping_dirs, sender=Entry)

#ping_links = ping_external_links(
#	content_attr='body_html',
#	url_attr='get_absolute_url',
#	filtr=lambda x: x.is_public
#)
#models.signals.post_save.connect(ping_links, sender=Entry)
