import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DailyFlow.settings")

from DailyFlow.wsgi import application

app = application
