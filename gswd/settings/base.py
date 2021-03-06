import os
import dj_database_url

here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
PROJECT_ROOT = here("..", "..")
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ("Kenneth Love", "kenneth@gettingstartedwithdjango.com"),
    ("Chris Jones", "chris@brack3t.com")
)

MANAGERS = ADMINS

DATABASES["default"] = dj_database_url.config()

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "America/Los_Angeles"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = root("media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = root("static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "http://static.gettingstartedwithdjango.com/"

# Additional locations of static files
STATICFILES_DIRS = (
    root("assets"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"
AWS_STORAGE_BUCKET_NAME = "static.gettingstartedwithdjango.com"
STATICFILES_STORAGE = "storages.backends.s3boto.S3BotoStorage"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    # ("django.template.loaders.cached.Loader", (
    #     "django.template.loaders.filesystem.Loader",
    #     "django.template.loaders.app_directories.Loader",
    # )),
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "social_auth.context_processors.social_auth_by_name_backends",
    "social_auth.context_processors.social_auth_backends",
    "social_auth.context_processors.social_auth_by_type_backends",
    "social_auth.context_processors.social_auth_login_redirect",
)

AUTHENTICATION_BACKENDS = (
    "social_auth.backends.contrib.github.GithubBackend",
    "django.contrib.auth.backends.ModelBackend"
)

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Espanol'),
)

LOCALE_PATHS = (
    root("locale"),
)

LOGIN_URL = "/login-form/"
LOGIN_REDIRECT_URL = "/"
LOGIN_ERROR_URL = "/login-error/"
SOCIAL_AUTH_COMPLETE_URL_NAME = "socialauth_complete"
SOCIAL_AUTH_ASSOCIATE_URL_NAME = "socialauth_associate_complete"

ROOT_URLCONF = "gswd.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "gswd.wsgi.application"

TEMPLATE_DIRS = (
    root("templates"),
)

DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.flatpages",
)

THIRD_PARTY_APPS = (
    "gunicorn",
    "south",
    "social_auth",
    "micawber.contrib.mcdjango",
    "storages",
    "raven.contrib.django",
)

OUR_APPS = (
    "lessons",
    "qa",
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + OUR_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}
