"""
Base settings to build other settings files upon.
"""
import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import environ

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

APPS_DIR = BASE_DIR / "arushop"
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env.bool("DJANGO_DEBUG", False)

TIME_ZONE = "UTC"

LANGUAGE_CODE = "en-us"

LANGUAGES = [
    ('en', _('English')),
    ('fa', _('Persian')),
]

SITE_ID = 1

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [str(BASE_DIR / "locale")]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

MOST_PORIARITY_APPS = ["markdownfield","jet"]

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "drf_spectacular",
    "drf_yasg",
]

LOCAL_APPS = [
    "arushop.users",
    "arushop.shop",
    "arushop.home",
    "arushop.blog",
    "arushop.search",
    "arushop.faq",
    "arushop.mail",
    "arushop.payment",
    "arushop.recommandation_system",
    "arushop.report",
    
    
]

INSTALLED_APPS = MOST_PORIARITY_APPS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIGRATION_MODULES = {"sites": "arushop.contrib.sites.migrations"}


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

AUTH_USER_MODEL = "users.User"

LOGIN_REDIRECT_URL = "users:redirect"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
LOGIN_URL = "account_login"


PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]


STATIC_ROOT = str(BASE_DIR / "staticfiles")

STATIC_URL = "/static/"

STATICFILES_DIRS = [str(APPS_DIR / "static")]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


MEDIA_ROOT = str(APPS_DIR / "media")

MEDIA_URL = "/media/"


TEMPLATES = [
    {

        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [str(APPS_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "arushop.users.context_processors.allauth_settings",
            ],
        },
    }
]

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"


CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = "DENY"

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)

EMAIL_TIMEOUT = 5

ADMIN_URL = "admin/"

ADMINS = [("""Mohammadreza Amani""", "more.amani@yahoo.com")]

MANAGERS = ADMINS

DJANGO_ADMIN_FORCE_ALLAUTH = env.bool("DJANGO_ADMIN_FORCE_ALLAUTH", default=False)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}


ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)

ACCOUNT_AUTHENTICATION_METHOD = "username"

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "mandatory"

ACCOUNT_ADAPTER = "arushop.users.adapters.AccountAdapter"

ACCOUNT_FORMS = {"signup": "arushop.users.forms.UserSignupForm"}

SOCIALACCOUNT_ADAPTER = "arushop.users.adapters.SocialAccountAdapter"

SOCIALACCOUNT_FORMS = {"signup": "arushop.users.forms.UserSocialSignupForm"}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

CORS_URLS_REGEX = r"^/api/.*$"

SPECTACULAR_SETTINGS = {
    "TITLE": "AruShop API",
    "DESCRIPTION": "Documentation of API endpoints of AruShop",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAdminUser"],
}
