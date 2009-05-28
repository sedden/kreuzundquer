from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class WYMEditor(forms.Textarea):
    class Media:
        js = (
            'js/jquery/jquery.js',
            'js/wymeditor/jquery.wymeditor.pack.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        self.attrs = {'class': 'wymeditor'}
        if attrs:
            self.attrs.update(attrs)
        super(WYMEditor, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(WYMEditor, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            jQuery('#id_%s').wymeditor({
                updateSelector: '.submit-row input[type=submit]',
                updateEvent: 'click',
                lang: '%s',
            });
            </script>''' % (name, self.language))

class markitUpEditor(forms.Textarea):
    class Media:
        js = (
            'js/jquery/jquery.js',
            'js/markitup/jquery.markitup.js',
            'js/markitup/sets/markdown/set.js',
            'js/markItUp_init.js',
        )
        css = (
            'js/markitup/skins/simple/style.css',
            'js/markitup/sets/markdown/style.css',
        )

    #def __init__(self, language=None, attrs=None):
    #    self.language = language or settings.LANGUAGE_CODE[:2]
    #    self.attrs = {'class': 'wymeditor'}
    #    if attrs:
    #        self.attrs.update(attrs)
    #    super(markitUpEditor, self).__init__(attrs)

    #def render(self, name, value, attrs=None):
    #    rendered = super(markitUpEditor, self).render(name, value, attrs)
    #    return rendered + mark_safe(u'''<script type="text/javascript">
    #        jQuery('#id_%s').wymeditor({
    #            updateSelector: '.submit-row input[type=submit]',
    #            updateEvent: 'click',
    #            lang: '%s',
    #        });
    #        </script>''' % (name, self.language))
