# Django settings for simplewiki project.

from os import path

PRJ_DIR = path.abspath(path.dirname(__file__))
PRJ_NAME = path.basename(PRJ_DIR)

DEBUG = False
TEMPLATE_DEBUG = DEBUG
FORCE_SCRIPT_NAME=""

APPEND_SLASH = False
PREPEND_WWW = True

DEFAULT_FROM_EMAIL = "webmaster@kreuzundquer-ev.de"

# Empfaenger fuer Fehlermeldungen
ADMINS = (
    ('Stefan Jenkner', 'stefan@jenkner.org'),
)

# Empfaenger fuer Kontakt-Formular
MANAGERS = (
    ('Michaela Richter', 'ela@kreuzundquer-ev.de'),
    ('Michaela Richter', 'ela-kolumbine@web.de'),
    ('Sebastian Meichssner', 'basti@kreuzundquer-ev.de'),
)


DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = PRJ_NAME       # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de'

DEFAULT_ENCODING='utf-8'

SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

#LANGUAGES = (
#	('de', _('German')),
#	('en', _('English')),
#)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = path.join(PRJ_DIR,'static')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^b@a&fmybr=g5&i#dg106f8-out^7v3ch&z-rb6c30pglh5)nn'

# Login
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
#    'dbtemplates.loader.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = PRJ_NAME+'.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    path.join(PRJ_DIR,'templates'),
)

MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/simple'
MARKITUP_PREVIEW_FILTER = ('markdown.markdown', {'safe_mode': True})

GRAVATAR_DEFAULT_IMAGE = MEDIA_URL + "img/gravatar.png"

ROBOTS_CACHE_TIMEOUT = 60*60*24

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    'django.contrib.syndication',
    'django.contrib.comments',
    'reversion',
    'blog',
    'flatpages',
    'contact_form',
    'markitup',
    'tagging',
    'gravatar',
    'robots',
)
