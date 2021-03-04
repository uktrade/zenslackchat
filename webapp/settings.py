"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import sys
import json
import logging
import binascii
from pathlib import Path

import environ
import sentry_sdk
import dj_database_url
from sentry_sdk.integrations.django import DjangoIntegration

from zenslackchat import botlogging


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOGGING = botlogging.config

VCAP_SERVICES = json.loads(os.environ.get('VCAP_SERVICES', "{}"))

DEBUG = False
if os.environ.get("DEBUG_ENABLED", "0").strip() == "1":
    sys.stderr.write("DEBUG_ENABLED=1 is set in environment!\n")
    DEBUG = True


DISABLE_MESSAGE_PROCESSING = False
if os.environ.get("DISABLE_MESSAGE_PROCESSING", "0").strip() == "1":
    # Stop handling messages, while this is set in the environment.
    sys.stderr.write("DISABLE_MESSAGE_PROCESSING is set in environment!\n")
    DISABLE_MESSAGE_PROCESSING = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

SECRET_KEY = os.environ.get(
    'WEBAPP_SECRET_KEY',
    # generate random one if not given for working development
    binascii.hexlify(os.urandom(64)).decode()
)

# Slack & Bot credentials:
SLACK_CLIENT_ID = os.environ.get('SLACK_CLIENT_ID', 'YOUR CLIENT ID')
SLACK_CLIENT_SECRET = os.environ.get(
    'SLACK_CLIENT_SECRET', 'YOUR CLIENT SECRET'
)
SLACK_BOT_USER_TOKEN = os.environ.get(
    'SLACK_BOT_USER_TOKEN', 'YOUR BOT USER TOKEN'
)
SLACK_VERIFICATION_TOKEN = os.environ.get(
    'SLACK_VERIFICATION_TOKEN', 'YOUR VERIFICATION TOKEN'
)
# where to exchange the request token for an access token:
SLACK_OAUTH_URI = os.environ.get(
    'SLACK_OAUTH_URI', 'https://slack.com/api/oauth.access'
)
# The base uri on which '/channel_id/message_id/' is added to form the direct
# link to the message on Slack:
SLACK_WORKSPACE_URI = os.environ.get(
    'SLACK_WORKSPACE_URI', 'https://<YOUR WORKSPACE>.slack.com/archives'
)


# The channel events we listen for and ignore all other events.
SRE_SUPPORT_CHANNEL = os.environ.get(
    'SRE_SUPPORT_CHANNEL', 'YOUR SUPPORT CHANNEL ID'
)

ZENDESK_CLIENT_IDENTIFIER = os.environ.get(
    'ZENDESK_CLIENT_IDENTIFIER', 'YOUR ZENDESK CLIENT UNIQUE IDENTIFIER'
)
ZENDESK_CLIENT_SECRET = os.environ.get(
    'ZENDESK_CLIENT_SECRET', 'YOUR ZENDESK CLIENT SECRET'
)
ZENDESK_SUBDOMAIN = os.environ.get(
    'ZENDESK_SUBDOMAIN', 'YOUR ZENDESK SUBDOMAIN'
)
ZENDESK_REDIRECT_URI = os.environ.get(
    'ZENDESK_REDIRECT_URI', 'YOUR URI FOR http(s)://<our host>/zendesk/oauth'
)
ZENDESK_TICKET_URI = os.environ.get(
    'ZENDESK_TICKET_URI', 'https://<YOUR SUBDOMAIN>.zendesk.com/agent/tickets'
)
ZENDESK_USER_ID = os.environ.get(
    'ZENDESK_USER_ID', '<The user id to assign new zendesk tickets to>'
)
ZENDESK_GROUP_ID = os.environ.get(
    'ZENDESK_GROUP_ID', '<The group id new zendesk tickets belong to>'
)
ZENDESK_WEBHOOK_USER = os.environ.get(
    'ZENDESK_WEBHOOK_USER', '<some random username>'
)
ZENDESK_WEBHOOK_TOKEN = os.environ.get(
    'ZENDESK_WEBHOOK_TOKEN', '<shared secret random string>'
)
ZENDESK_AGENT_EMAIL = os.environ.get(
    'ZENDESK_AGENT_EMAIL', '<email of zenslackchat agent>'
)


PAGERDUTY_OAUTH_URI = os.environ.get(
    'PAGERDUTY_OAUTH_URI', 'https://app.pagerduty.com/oauth/token'
)
PAGERDUTY_CLIENT_IDENTIFIER = os.environ.get(
    'PAGERDUTY_CLIENT_IDENTIFIER', 'YOUR PAGER DUTY CLIENT UNIQUE IDENTIFIER'
)
PAGERDUTY_CLIENT_SECRET = os.environ.get(
    'PAGERDUTY_CLIENT_SECRET', 'YOUR PAGER DUTY CLIENT SECRET'
)
PAGERDUTY_REDIRECT_URI = os.environ.get(
    'PAGERDUTY_REDIRECT_URI', 'URI FOR http(s)://<our host>/pagerduty/oauth'
)
PAGERDUTY_ESCALATION_POLICY_ID = os.environ.get(
    'PAGERDUTY_ESCALATION_POLICY_ID', 'PagerDuty Policy ID'
)

# Used to work out our external URI for redirects. Also used as the entry in
# ALLOWED_HOSTS.
PAAS_FQDN = os.environ.get(
    'PAAS_FQDN', 'The fully qualified domain name of the PaaS webapp'
)

# Who can connect:
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1"
]
PAAS_FQDN = os.environ.get("PAAS_FQDN", "").strip()
if PAAS_FQDN:
    ALLOWED_HOSTS.insert(0, PAAS_FQDN)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'zenslackchat.apps.ZenSlackChatConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'webapp.wsgi.application'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {}
DATABASES['default'] = dj_database_url.config()


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

LOGIN_REDIRECT_URL = '/'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Redis & Celery
if 'redis' in VCAP_SERVICES:
    REDIS_URL = VCAP_SERVICES['redis'][0]['credentials']['uri']
    REDIS_CELERY_URL = f'{REDIS_URL}?ssl_cert_reqs=CERT_REQUIRED'

else:
    REDIS_URL = os.environ['REDIS_URL']
    REDIS_CELERY_URL = REDIS_URL

CELERY_BROKER_URL = REDIS_CELERY_URL
# no results as I'm just running a report once a day and it should just work.
# result_backend = REDIS_CELERY_URL
accept_content = ['application/json']
task_serializer = 'json'
result_serializer = 'json'
task_always_eager = False

# Set the name for the app in logging:
DLFE_APP_NAME = 'ZenSlackChat'

ENV_FILE = os.path.join(BASE_DIR, '.env')
if os.path.exists(ENV_FILE):
    logging.getLogger(__name__).warning(
        "Using .env file to override configuration."
    )
    environ.Env.read_env(ENV_FILE)

# Sentry set up:
SENTRY_DSN = os.environ.get("SENTRY_DSN", None)
if SENTRY_DSN:
    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()])
else:
    logging.getLogger(__name__).info("SENTRY_DSN not set. Sentry is diabled.")
