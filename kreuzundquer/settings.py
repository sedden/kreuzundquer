import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DEBUG = True
TEMPLATE_DEBUG = DEBUG
FORCE_SCRIPT_NAME=""

APPEND_SLASH = False
#PREPEND_WWW = True

EMAIL_SUBJECT_PREFIX = "[KUQ] "
SERVER_EMAIL = "webmaster@kreuzundquer-ev.de"
DEFAULT_FROM_EMAIL = "webmaster@kreuzundquer-ev.de"

# Empfaenger fuer Fehlermeldungen
ADMINS = (
    ('Stefan Jenkner', 'stefan@kreuzundquer-ev.de'),
)

# Empfaenger fuer Kontakt-Formular
MANAGERS = (
    ('Michaela Richter', 'ela@kreuzundquer-ev.de'),
    ('Stefan Jenkner', 'stefan@kreuzundquer-ev.de'),
    ('Susann Jenkner', 'susann@kreuzundquer-ev.de'),
)

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'kreuzundquer.db',       # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Parse database configuration from $DATABASE_URL
import dj_database_url
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config()


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

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

#LANGUAGES = (
#	('de', _('German')),
#	('en', _('English')),
#)

# Date and Time
# http://docs.djangoproject.com/en/1.1/ref/templates/builtins/#ttag-now
DATE_FORMAT = 'd. F'
#DATETIME_FORMAT = ''
TIME_FORMAT = 'H\:i'
#YEAR_MONTH_FORMAT = ''
#MONTH_DAY_FORMAT = ''

# Static asset configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'sitestatic')
#STATIC_ROOT = 'static'
STATIC_URL = '/static/'

# Additional static filed
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static'),
)


AWS_QUERYSTRING_AUTH = False
AWS_S3_SECURE_URLS = False
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']

#MEDIA_ROOT = path.join(PRJ_DIR,'static/media')
MEDIA_URL = 'http://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
#MEDIA_URL = 'http://%s.s3-website.eu-west-1.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
#MEDIA_URL = '/media/'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^b@a&fmybr=g5&i#dg106f8-out^7v3ch&z-rb6c30pglh5)nn'

# Login
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
    'dbtemplates.loader.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'kreuzundquer.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_SKIN = 'markitup/skins/simple'
MARKITUP_PREVIEW_FILTER = ('markdown.markdown', {'safe_mode': True})

#GRAVATAR_DEFAULT_IMAGE = 'http://www.kreuzundquer-ev.de' + MEDIA_URL + 'img/gravatar.png'
GRAVATAR_DEFAULT_IMAGE = MEDIA_URL + 'img/gravatar.png'
GRAVATAR_URL_PREFIX = 'http://en.gravatar.com/'

ROBOTS_CACHE_TIMEOUT = 60*60*24

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.syndication',
    'django.contrib.comments',
    'storages',
    'reversion',
    'blog',
    'flatpages',
    'contact_form',
    'markitup',
    'tagging',
    'gravatar',
    'robots',
    'dbtemplates',
    'imagekit',
    'basic.media',
    'basic.inlines',
    'basic.places',
    'basic.events',
)
