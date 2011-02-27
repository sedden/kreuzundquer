from django.contrib import admin
from basic.events.models import *
from django.core.urlresolvers import reverse

from markitup.widgets import MarkItUpWidget

class EventTimeInline(admin.StackedInline):
    model = EventTime
    fk = 'event'

class EventAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'place', 'created')
    inlines = [
        EventTimeInline
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'description':
            return db_field.formfield(widget=MarkItUpWidget())
        return super(EventAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Event, EventAdmin)
