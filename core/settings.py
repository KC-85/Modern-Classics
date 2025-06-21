# core/settings.py

from pathlib import Path
import os
from decouple import AutoConfig, Csv
import dj_database_url
from datetime import timedelta

# === Project Paths & Config ===
BASE_DIR = Path(__file__).resolve().parent.parent
config   = AutoConfig(search_path=BASE_DIR)

# === Environment & Debug ===
# Set ENVIRONMENT=production locally or on Heroku to toggle settings
ENVIRONMENT = config("ENVIRONMENT", default="development")
DEBUG       = ENVIRONMENT != "production"
IS_HEROKU   = "DYNO" in os.environ

# === Security & Hosts ===
SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="127.0.0.1,localhost,0.0.0.0,https://modern-classics-b10468fd6f55.herokuapp.com",
    cast=Csv(),
)
CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    default="https://127.0.0.1,https://localhost,https://modern-classics-b10468fd6f55.herokuapp.com",
    cast=Csv(),
)

# === HTTPS Security (Heroku Only) ===
SECURE_SSL_REDIRECT       = IS_HEROKU
SESSION_COOKIE_SECURE     = IS_HEROKU
CSRF_COOKIE_SECURE        = IS_HEROKU
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS             = "DENY"
SECURE_REFERRER_POLICY      = "strict-origin-when-cross-origin"
DEBUG_PROPAGATE_EXCEPTIONS  = False

# === Installed Apps ===
INSTALLED_APPS = [
    # Django Core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",       # required by allauth
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Brute Force Protection
    "axes",

    # Authentication
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    # Media & Static
    "cloudinary",
    "cloudinary_storage",
    "whitenoise.runserver_nostatic",

    # Your Apps
    "apps.common.apps.CommonConfig",
    "apps.users.apps.UsersConfig",
    "apps.showroom.apps.ShowroomConfig",
    "apps.orders.apps.OrdersConfig",
    "apps.trailer.apps.TrailerConfig",
    "apps.delivery.apps.DeliveryConfig",

    # Crispy
    "crispy_forms",
    "crispy_bootstrap5",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Tell Django to use your custom user model
AUTH_USER_MODEL = "users.CustomUser"

SITE_ID = 1

# === Middleware ===
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "axes.middleware.AxesMiddleware",
]

# === URL Configuration ===
ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"

# === Templates ===
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# === Database (Postgres via DATABASE_URL) ===
DATABASE_URL = config("DATABASE_URL", default=None)
if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is missing.")
DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        ssl_require=IS_HEROKU,
    )
}

# === Password Validators ===
AUTH_PASSWORD_VALIDATORS = [
    { "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator" },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": { "min_length": 12 }
    },
    { "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator" },
    { "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator" },
]

# === Internationalization ===
LANGUAGE_CODE = "en-us"
TIME_ZONE     = "UTC"
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

# === Static & Media ===
STATIC_URL = "/static/"

# Tell Django where to find *additional* static assets in dev:
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_URL        = "/static/"
STATIC_ROOT       = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL         = "/media/"
MEDIA_ROOT        = BASE_DIR / "media"

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": config("CLOUDINARY_CLOUD_NAME"),
    "API_KEY":    config("CLOUDINARY_API_KEY"),
    "API_SECRET": config("CLOUDINARY_API_SECRET"),
}

# === Authentication ===
AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

LOGIN_URL          = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

# === django-allauth Settings ===
ACCOUNT_LOGIN_METHOD            = "username_email"
ACCOUNT_USERNAME_REQUIRED       = True
ACCOUNT_EMAIL_REQUIRED          = True
ACCOUNT_SIGNUP_FIELDS           = ["username*", "email*"]
ACCOUNT_EMAIL_VERIFICATION      = "mandatory"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# === Axes (Brute Force Protection) ===
AXES_ENABLED                    = True
AXES_FAILURE_LIMIT              = config("AXES_FAILURE_LIMIT", default=3, cast=int)
AXES_COOLOFF_TIME               = timedelta(hours=config("AXES_COOLOFF_HOURS", default=1, cast=int))
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True
AXES_RESET_ON_SUCCESS           = True

# === Stripe Configuration ===
STRIPE_PUBLISHABLE_KEY = config("STRIPE_PUBLISHABLE_KEY", default="")
STRIPE_SECRET_KEY      = config("STRIPE_SECRET_KEY", default="")
STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET")

# === Default Primary Key Field Type ===
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# === Logging (Production only) ===
if not DEBUG:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "file": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "filename": BASE_DIR / "django_error.log",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file"],
                "level": "ERROR",
                "propagate": True,
            },
        },
    }
