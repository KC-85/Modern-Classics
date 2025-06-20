# core/wsgi.py
import os
from dotenv import load_dotenv

load_dotenv()   # this will read the .env into os.environ

from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.environ.get("DJANGO_SETTINGS_MODULE", "core.settings"),
)

application = get_wsgi_application()
