# core/settings/development.py

import os
from datetime import timedelta
import dj_database_url
from .base import *

# ─── DEBUG & HOSTS ───────────────────────────────────────────
DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# ─── DATABASE ───────────────────────────────────────────────
DATABASES = {
    "default": dj_database_url.config(
        default=get_env(
            "DATABASE_URL",
            "postgres://postgres:password@localhost:5432/modern_classics_dev"
        ),
        conn_max_age=0,       # no persistent connections in dev
        ssl_require=False,    # no SSL requirement locally
    )
}

# ─── EMAIL ──────────────────────────────────────────────────
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = get_env("EMAIL_HOST", "smtp.mailtrap.io")
EMAIL_PORT = int(get_env("EMAIL_PORT", 587))
EMAIL_HOST_USER = get_env("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = get_env("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = get_env("EMAIL_USE_TLS", "True") == "True"
# EMAIL_USE_SSL = get_env("EMAIL_USE_SSL", "False") == "True"

DEFAULT_FROM_EMAIL = get_env("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)
SERVER_EMAIL       = get_env("SERVER_EMAIL", EMAIL_HOST_USER)

# Django-axes Configuration 
# Lock out after 3 failed login attempts
AXES_FAILURE_LIMIT = 3

# Automatically unlock after 1 hour
AXES_COOLOFF_TIME = timedelta(hours=1)

# Count failures by both username and IP (optional; default is True)
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True

# Optional Dev Tools
# e.g. Django Debug Toolbar
# INSTALLED_APPS += ["debug_toolbar"]
# MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
# INTERNAL_IPS = ["127.0.0.1"]
