from pathlib import Path
import os

# Base directory of the project (root)
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ Security settings
SECRET_KEY = 'django-insecure-$d*%(wjxpro3$a*u&oq**qt-5#nuk0r&ug$%h-v%2yk8d^5!by'  # 🔒 Never expose in production
DEBUG = True  # ⚠️ Set to False in production
ALLOWED_HOSTS = []  # ⚠️ Add domain/IP in production (e.g., ['example.com'])

# Installed apps – core Django + third-party + local apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local app
    'flights',

    # Third-party apps
    'rest_framework',
    'corsheaders',
]

# Middleware stack – includes CORS support
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be placed at the top for CORS to work properly
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'flight_project.urls'

# Template engine settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can specify template directories here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application entry point (used in production)
WSGI_APPLICATION = 'flight_project.wsgi.application'

# Database configuration (default: SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization and timezone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static file settings
STATIC_URL = 'static/'

# Default field type for primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings – allow all origins (⚠️ only for development)
CORS_ALLOW_ALL_ORIGINS = True
