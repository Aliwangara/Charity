from .base import *
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()


ALLOWED_HOSTS = ["https://charity-production.up.railway.app","https://charity-production.up.railway.app"]
CSRF_TRUSTED_ORIGINS = ["https://charity-production.up.railway.app","https://charity-production.up.railway.app"]

# DATABASES = {
#     'default': {
#                 'ENGINE': 'django.db.backends.postgresql',
#                 'NAME': 'railway',
#                 'USER': 'postgres',
#                 'PASSWORD': os.environ.get('DB_PASSWORD'),
#                 'HOST': 'roundhouse.proxy.rlwy.net',
#                 'PORT': '5432',
#                 'Default': dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=1800)
#     }
# }



DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'defaultdb',
        'USER': 'avnadmin',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'smilesdb-wangaraali56-4122.l.aivencloud.com',
        'PORT': '11603',
        # 'gssencmode':'disable'
    }
}

print(DATABASES)
