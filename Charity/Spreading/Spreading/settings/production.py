from .base import *
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()


ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'railway',
                'USER': 'postgres',
                'PASSWORD': os.environ.get('DB_PASSWORD'),
                'HOST': 'postgres.railway.internal',
                'PORT': '5432',
                'Default': dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=1800)
    }
}
