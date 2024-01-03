
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*x_6@bohce)k$1nfupg@w)-o=#tqlgcs0xmg8v#1+1*+z1r2yo'

WEBSITE_HOSTNAME = os.environ.get('WEBSITE_HOSTNAME', None)

DEBUG = WEBSITE_HOSTNAME == None

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = [WEBSITE_HOSTNAME]
    CSRF_TRUSTED_ORIGINS = [f'https://{WEBSITE_HOSTNAME}']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chat.apps.ChatConfig',
    'simple_chatbot',
    'crispy_forms',
    "crispy_bootstrap4",
    'user_app',
]
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'Chatbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Chatbot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['AZURE_DB_NAME'],
        'HOST': os.environ['AZURE_DB_HOST'],
        'PORT': os.environ['AZURE_DB_PORT'],
        'USER': os.environ['AZURE_DB_USER'],
        'PASSWORD': os.environ['AZURE_DB_PASSWORD'],
        
    }
}




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


DEFAULT_FILE_STORAGE = 'Chatbot.storage.AzureMediaStorage'
STATICFILES_STORAGE = 'Chatbot.storage.AzureStaticStorage'

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

AZURE_ACCOUNT_NAME = "c2064645"
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'

# Adjust the following settings for Azure Storage
AZURE_ACCOUNT_KEY = 'vuj4vqZysdMrrVMlPo5B51TkbPR3Tw5+Fif/NUm9hower41n0t+PJqCuhQefkH4mPPTBHOeYS86D+AStBQ9iHQ=='  # Replace with your Azure Storage account key
AZURE_CONTAINER = 'c2064645'  # Replace with your Azure Storage container name

AZURE_BLOB_HEADERS = {
    'x-ms-blob-cache-control': 'max-age=3600',  # Adjust cache settings as needed
    'Access-Control-Allow-Origin': '*',  # Set appropriate CORS policy
}

AZURE_OVERWRITE_FILES = True  # Set to True to overwrite existing files during collectstatic


#STATIC_URL = '/static/'
#MEDIA_ROOT = BASE_DIR / 'media'
#MEDIA_URL = '/media/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, 'static'),
#]



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SIMPLE_CHATBOT = {
    'responses': [
        ("chat.responses.GreetingResponse", "Greeting"),
        ("chat.responses.GoodbyeResponse", "Goodbye"),
        ("chat.responses.MentalHealthAdviserResponse", "Name"),
        ("chat.responses.StressManagementResponse", "Stress"),
        ("chat.responses.AnxietySupportResponse", "Anxiety"),
        ("chat.responses.LonelinessSupportResponse", "Loneliness"),
        ("chat.responses.FriendSupportResponse", "Friend Support"),
        ("chat.responses.SeriousConcernResponse", "Serious Concern"),
        ("chat.responses.SelfConfidenceBuildingResponse", "Self Confidence"),
        ("chat.responses.OverwhelmedFeelingResponse", "Overwhelmed Feeling"),
        ("chat.responses.EncourageReportingBullyingResponse", "Encourage Reporting"),
        ("chat.responses.OopsWhatHappenedResponse", "OopsWhatHappenedResponse"),
        ("chat.responses.SorryAboutExperienceResponse", "SorryAboutExperienceResponse"),
        ("chat.responses.SorryOnceAgainResponse", "SorryOnceAgainResponse"),
        ("chat.responses.YouDontDeserveResponse", "YouDontDeserveResponse"),
        ("chat.responses.CopingStrategiesResponse", "CopingStrategiesResponse"),
        ("chat.responses.YesYouCanResponse", "YesYouCanResponse"),
        ("chat.responses.BullyingFactorsResponse", "BullyingFactorsResponse"),
    ],
}

