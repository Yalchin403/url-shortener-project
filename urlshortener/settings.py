"""
Django settings for urlshortener project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '02r96cvjhqat+x3(m&u!@0firtuqiqw+=hq^&ho6z1+l25_=om'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'accounts',
    'backend',
    'paste_zone',
    'ckeditor',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urlshortener.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['urlshortener/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'urlshortener.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'urlshortener/static')
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_CONFIGS = {
         # django-ckeditor uses the default configuration by default
    'default': {
                 # Editor width adaptive
        'width':'auto',
        'height':'250px',
                 # Tab key to convert the number of spaces
        'tabSpaces': 4,
                 # Toolbar style
        'toolbar': 'Custom',
                 # Toolbar button
        'toolbar_Custom': [
                         # Emoji code block
            ['Smiley', 'CodeSnippet'],
            ['Format'],
                         # Font style
            ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
                         # font color 
            ['TextColor', 'BGColor'],
                         # Link
            ['Link', 'Unlink'],
                         # List
            ['NumberedList', 'BulletedList'],
                         # Maximize
            ['Maximize'],
            ['Source'],
            ['Table', 'Tabletools'],
            ['Image']
        ],
        # Add code block plugin
        'codeSnippet_languages': {
            'python': 'Python <3',
            'c': 'C',
            'cpp': 'C++',
            'csharp': 'C#',
            'bash': 'Bash',
            'aspnet': 'ASP.NET',
            'dart': 'Dart',
            'docker': 'Docker',
            'flutter': 'Flutter',
            'fortran': 'Fortran',
            'haskel': 'Haskel',
            'markup': 'HTML',
            'http': 'HTTP',
            'git': 'Git',
            'go': 'Golang',
            'java': 'Java',
            'javascript': 'JavaScript',
            'makefile':'Makefile',
            'matlab': 'MATLAB',
            'nginx': 'Nginx',
            'pascal': 'Pascal',
            'perl': "Perl",
            'php': 'PHP',
            'rust': 'Rust',
            'ruby': 'Ruby',
            'r': 'R',
            'sas': 'SAS',
            'scala': 'Scala',
            'scheme': 'Scheme',
            'sql': 'SQL',
            'swift': 'Swift',
            'vim': 'Vim',
            'yml': 'YML'
        },
       
        'extraPlugins': ','.join(['codesnippet', 'prism', 'widget', 'lineutils', 'table', 'clipboard', 'format',
                                  'image', 'tabletools']),

    }
}

try:
    from .local_settings import *
except ImportError:
    pass
