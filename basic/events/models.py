import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from tagging.fields import TagField
from basic.places.models import Place


class Event(models.Model):
    """Event model"""
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), )
    place = models.ForeignKey(Place, blank=True, null=True, verbose_name=_('place'))
    one_off_place = models.CharField(_('one of place'), max_length=200, blank=True)
    description = models.TextField(_('description'), blank=True)
    submitted_by = models.ForeignKey(User, blank=True, null=True,  verbose_name=_('user'))
    tags = TagField()
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        verbose_name = _('event')
        verbose_name_plural = _('events')
        db_table = 'events'

    def __unicode__(self):
        return self.title


class EventTime(models.Model):
    """EventTime model"""
    event = models.ForeignKey(Event, related_name='event_times', verbose_name=_('event'))
    start = models.DateTimeField(_('start'))
    end = models.DateTimeField(_('end'), blank=True, null=True)
    is_all_day = models.BooleanField(_('is all day'), default=False)

    class Meta:
        verbose_name = _('event time')
        verbose_name_plural = _('event times')
        db_table = 'event_times'

    @property
    def is_past(self):
        NOW = datetime.date.now()
        if self.start < NOW:
            return True
        return False

    def __unicode__(self):
        return u'%s' % self.event.title

    @permalink
    def get_absolute_url(self):
        return ('event_detail', None, {
            'year': self.start.year,
            'month': self.start.strftime('%m'),
            'day': self.start.day,
            'slug': self.event.slug,
            'id': self.id
        })
