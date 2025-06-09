# core/settings/base.py

import os
from pathlib import Path
import dj_database_url

# ─── PATHS ─────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent.parent

def get_env(var_name, default=None):
    """Helper to fetch environment variables or return a default."""
    return os.environ.get(var_name, default)

# ─── SECURITY & HOSTS ─────────────────────────────────────────
SECRET_KEY = get_env("SECRET_KEY", "change-me-in-env")
DEBUG      = True
# Comma-separated list, e.g. "localhost,example.com"
ALLOWED_HOSTS = get_env("ALLOWED_HOSTS", "").split(",")

# ─── INSTALLED APPS ───────────────────────────────────────────
INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # Third-party
    "axes",                   # brute-force protection
    "allauth",                # authentication & 2FA
    "allauth.account",
    "allauth.socialaccount",
    "cloudinary",             # Cloudinary media storage
    "cloudinary_storage",
    "whitenoise.runserver_nostatic",

    # Your apps
    "apps.common",
    "apps.users",
    "apps.showroom",
    "apps.orders",
]

SITE_ID = int(get_env("SITE_ID", 1))

# ─── MIDDLEWARE ───────────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",    # static files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "axes.middleware.AxesMiddleware",                # lockout protection
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ─── URL & WSGI/ASGI ──────────────────────────────────────────
ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"

# ─── TEMPLATES ─────────────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # required by allauth
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ─── DATABASE (PostgreSQL via DATABASE_URL) ────────────────────
DATABASES = {
    "default": dj_database_url.config(
        default=get_env(
            "DATABASE_URL",
            "postgres://postgres:password@localhost:5432/modern_classics_dev"
        ),
        conn_max_age=600,
        ssl_require=not DEBUG,
    )
}

# ─── PASSWORD VALIDATORS ──────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},    #noqa
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},    #noqa
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},    #noqa
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},    #noqa
]

# ─── INTERNATIONALIZATION ─────────────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE     = "UTC"
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

# ─── STATIC & MEDIA FILES ─────────────────────────────────────
STATIC_URL        = "/static/"
STATICFILES_DIRS  = [BASE_DIR / "static"]
STATIC_ROOT       = BASE_DIR / "staticfiles"

MEDIA_URL         = "/media/"
MEDIA_ROOT        = BASE_DIR / "media"

# Cloudinary storage for media
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": get_env("CLOUDINARY_CLOUD_NAME"),
    "API_KEY":    get_env("CLOUDINARY_API_KEY"),
    "API_SECRET": get_env("CLOUDINARY_API_SECRET"),
}

# ─── AUTHENTICATION BACKENDS ─────────────────────────────────
AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",                           # brute-force guard
    "django.contrib.auth.backends.ModelBackend",           # default
    "allauth.account.auth_backends.AuthenticationBackend", # django-allauth
]

# django-allauth settings
LOGIN_REDIRECT_URL                    = "/"
ACCOUNT_AUTHENTICATION_METHOD         = "email"
ACCOUNT_EMAIL_REQUIRED                = True
ACCOUNT_EMAIL_VERIFICATION            = "optional"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION   = True

# ─── STRIPE CONFIGURATION ────────────────────────────────────
# Install stripe with: pip install stripe
STRIPE_PUBLISHABLE_KEY = get_env("STRIPE_PUBLISHABLE_KEY", "")
STRIPE_SECRET_KEY      = get_env("STRIPE_SECRET_KEY", "")
# If you wish to initialize the Stripe library here:
# import stripe
# stripe.api_key = STRIPE_SECRET_KEY
