import dj_database_url
import os
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
ALLOWED_HOSTS = ['surdatum-app.onrender.com', 'localhost', '127.0.0.1']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'corsheaders',
    'maps',
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
CORS_ALLOW_ALL_ORIGINS = True
