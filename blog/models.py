from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
#from django.contrib.comments.moderation import CommentModerator, moderator

from datetime import time, date, datetime
from time import strptime

from tagging.models import Tag
from tagging.fields import TagField

from blog.fields import MarkdownTextField

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

#class EntryModerator(CommentModerator):
#	email_notification = True
#	enable_field = 'enable_comments'
#moderator.register(Entry, EntryModerator)
